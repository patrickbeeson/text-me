from flask import Flask, request, redirect, url_for
from twilio.rest import TwilioRestClient
from PIL import Image, ImageDraw, ImageFont
import time


app = Flask(__name__, static_folder='static', static_url_path='')

client = TwilioRestClient(
    account='ACb01b4d6edfb1b41a8b80f5fed2c19d1a',
    token='97e6b9c0074b2761eff1375fb088adda'
)


@app.route('/', methods=['GET', 'POST'])
def send_image():
    if request.method == 'GET':
        return 'The deployment worked! Now copy your browser URL into the' + \
               ' Twilio message text box for your phone number.'
    sender_number = request.form.get('From', '')
    twilio_number = request.form.get('To', '')
    user_text = request.form.get('Body', '')
    image_url, msg_text = mod_photo(user_text)
    send_mms_twiml(image_url, msg_text, sender_number, twilio_number)
    return 'ok'


def mod_photo(user_text):
    base = Image.open('static/images/portland.jpg').convert('RGBA')

    txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype('static/fonts/Gobold.ttf', 16)

    d = ImageDraw.Draw(txt)

    d.text((25, 25), '{}...'.format(user_text), font=fnt, fill=(255, 255, 255, 255))

    image = Image.alpha_composite(base, txt)

    image.save('static/images/portland_{}.jpg'.format(user_text))

    try:
        msg_text = 'Imagine yourself in Portland!'
        image_url = 'http://12dcb913.ngrok.com/images/portland_{}.jpg'.format(user_text)
    except:
        msg = "Sorry, we couldn't pull a kitten, " + \
              "here's a dinosaur instead!"
        image_url = "https://farm1.staticflickr.com/46/" + \
                    "154877897_a299d80baa_b_d.jpg"

    return image_url, msg_text


def send_mms_twiml(image_url, msg_text, sender_number, twilio_number):
    client.messages.create(
        to=sender_number,
        from_=twilio_number,
        body=msg_text,
        media_url=image_url
    )

if __name__ == "__main__":
    app.run(debug=True)

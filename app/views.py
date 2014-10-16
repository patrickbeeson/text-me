from PIL import Image, ImageDraw, ImageFont
import datetime
from twilio.rest import TwilioRestClient

from flask import Flask, request
from app import app
from config import TWILIO_ACCOUNT, TWILIO_PASSWORD

client = TwilioRestClient(TWILIO_ACCOUNT, TWILIO_PASSWORD)


@app.route('/', methods=['GET', 'POST'])
def send_image():
    """
    Sends the text and image back to the original sender.
    """
    if request.method == 'GET':
        return 'The deployment worked! Now copy your browser URL into the' + \
               ' Twilio message text box for your phone number.'
    sender_number = request.form.get('From', '')
    twilio_number = request.form.get('To', '')
    user_text = request.form.get('Body', '').strip().split()[0]
    image_url, msg_text = mod_photo(user_text)
    send_mms_twiml(image_url, msg_text, sender_number, twilio_number)
    return 'ok'


def mod_photo(user_text):
    """
    Modifies a base image to add the sender's text (ideally, their name)
    """
    base = Image.open('app/static/images/original/chatsters_poster.png').convert('RGBA')

    txt = Image.new('RGBA', base.size, (143, 83, 157, 0))

    fnt = ImageFont.truetype('app/static/fonts/GothamRounded-Bold.otf', 86)

    d = ImageDraw.Draw(txt)

    base_w, base_h = (640, 1136)
    text_w, text_h = d.textsize(user_text, fnt)

    d.text(
        (((base_w-text_w)/2), 305),
        '{}'.format(user_text),
        font=fnt,
        fill=(143, 83, 157, 255)
    )

    image = Image.alpha_composite(base, txt)

    image_time_stamp = datetime.datetime.now()

    image.save('app/static/images/changed/chatsters_poster_{}_{}.png'.format(
        user_text,
        image_time_stamp.strftime('%y_%m_%d_%I%M%S')
        )
    )

    try:
        msg_text = 'Thanks for the text {}! Here\'s your custom phone wallpaper.'.format(user_text)
        image_url = 'http://dev.thevariable.com/static/images/changed/chatsters_poster_{}_{}.png'.format(
            user_text,
            image_time_stamp.strftime('%y_%m_%d_%I%M%S')
        )
    except:
        msg_text = "#ohno! We had trouble creating your image. " + \
            "Here's a cute kitten instead!"
        image_url = "http://placekitten.com/g/640/1136"

    return image_url, msg_text


def send_mms_twiml(image_url, msg_text, sender_number, twilio_number):
    """
    Creates the actual message object.
    """
    client.messages.create(
        to=sender_number,
        from_=twilio_number,
        body=msg_text,
        media_url=image_url
    )

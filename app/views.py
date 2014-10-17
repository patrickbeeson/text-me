from PIL import Image, ImageDraw, ImageFont
import datetime
import os
from twilio.rest import TwilioRestClient

from flask import Flask, request
from . import app

account = app.config['TWILIO_ACCOUNT']
token = app.config['TWILIO_TOKEN']
site_url = app.config['SITE_URL']
static_path = app.config['STATIC_PATH']

client = TwilioRestClient(
    account=account,
    token=token
)


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
    base = Image.open(
        static_path + 'static/images/original/place_kitten.jpeg'
    ).convert('RGBA')

    txt = Image.new('RGBA', base.size, (143, 83, 157, 0))

    fnt = ImageFont.truetype(
        static_path + 'static/fonts/OpenSans-Bold.ttf', 86
    )

    d = ImageDraw.Draw(txt)

    base_w, base_h = (640, 1136)
    text_w, text_h = d.textsize(user_text, fnt)

    d.text(
        (((base_w-text_w)/2), 295),
        '{}'.format(user_text),
        font=fnt,
        fill=(143, 83, 157, 255)
    )

    image = Image.alpha_composite(base, txt)

    image_time_stamp = datetime.datetime.now()

    image.save(
        static_path + 'static/images/changed/place_kitten_{}_{}.jpeg'.format(
            user_text,
            image_time_stamp.strftime('%y_%m_%d_%I%M%S')
        )
    )

    try:
        msg_text = (
            "Thanks, {}. Hope you liked my kitten :) "
            "Visit {} to search for more kittens!".format(
                user_text,
                'http://google.com'
            )
        )
        image_url = (
            '{}static/images/changed/place_kitten_{}_{}.jpeg'.format(
                site_url,
                user_text,
                image_time_stamp.strftime('%y_%m_%d_%I%M%S')
            )
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

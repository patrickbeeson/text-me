from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    """ Respond to incoming calls with a SMS """

    resp = twilio.twiml.Response()

    if body == '#bff':
        resp.message('#awesome')
        resp.message("What's your name?")
    else:
        resp.message('#lame')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

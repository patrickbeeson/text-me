from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    """ Respond to incoming calls with a SMS """

    resp = twilio.twiml.Response()
    resp.message("Hello! Thanks for texting me!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

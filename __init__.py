from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    """ Respond to incoming calls with a SMS """

    body = request.values.get('Body', None).lower()

    resp = twilio.twiml.Response()

    if body == '#bff':
        resp.message('#awesome')
    elif not "play date" in body:
        resp.message("Let's do it! Ask your parents first, though!")
    else:
        resp.message("#lame")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

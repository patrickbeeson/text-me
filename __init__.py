from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    """ Respond to incoming calls with a SMS """

    body = request.values.get('Body', None)

    resp = twilio.twiml.Response()

    if body == '#bff':
        resp.message('#awesome')
        resp.message("What's your name?")
    else:
        resp.message("#lame")

    user_name = request.values.get('Body', None)

    resp.message("It's great to meet you {name}!".format(name=user_name))
    resp.message("Wanna set up a play date?")

    play_date_response = request.values.get('Body', None)
    if play_date_response.lower() == 'yes':
        resp.message("That's great! "
                     "Get your parent's permission, "
                     "and go to http://chatsters.com.")
    elif play_date_response.lower() == 'no':
        resp.message("Too bad. Maybe another time!")
    else:
        resp.message('#lame')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

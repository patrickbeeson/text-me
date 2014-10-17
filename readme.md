# Text Me readme

*Author: Patrick Beeson, patrickbeeson@gmail.com*

## Description

Takes a person's first name from an SMS, and returns a custom image incorporating their name with an accompanying message.

This app uses Twilio's API; sign up for a free account at [http://twilio.com](http://twilio.com).

### Structure

This app uses a simple Flask structure with a standard config file, init and views.

The majority of the logic, as well as static files, are in the app directory.

You can run the Flask development server for this app using `run.py`.

## Usage

Perform the following steps to run this application locally:

1.  Download or clone the repository to your local computer
2.  Install the requirements from `requirements.txt` (ideally within virtualenv)
3.  Sign up for a Twilio account
4.  Update `config.py` with your account credentials and other info, such as URLs and paths. You'll also want to set your environment variables for the appropriate config settings.
5.  Use [ngrok](https://ngrok.com/) to create a publically-accessible dev server to allow Twilio to see your app
6.  Run `python run.py` to fire up the Flask dev server using the port specified with ngrok

You'll also want to adjust `views.py` to change out the original image and other attributes such as font and colors and positioning, etc. Ideally, these would be variables in config.

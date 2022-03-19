import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

accountSid = os.environ.get("TWILIO_ACCOUNTSID")
authToken = os.environ.get("TWILIO_AUTH_TOKEN")
_from = os.environ.get("TWILIO_NUM")
client = Client(accountSid, authToken);

_body = 'hi!!!'
_to = '+15194762084'

message = client.messages.create(
                            body=_body,
                            from_=_from,
                            to=_to
                            )

print(message.sid)

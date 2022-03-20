import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

accountSid = os.environ.get("TWILIO_ACCOUNTSID")
authToken = os.environ.get("TWILIO_AUTH_TOKEN")
messagingServiceSid = os.environ.get("TWILIO_SERVICE_SID")
client = Client(accountSid, authToken)
_to = os.environ.get("TWILIO_USER")

# accept incoming SMS and evaluate the response based on the text body
# FUTURE: grab transcriptions from database
@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
	# respond to txt w/ specific txt msg
	body = request.values.get('Body', None)
	if body == 'सम्बन्ध':
		message = client.messages.create(
		                            messaging_service_sid=messagingServiceSid,
		                            body='Welcome to Sambandh. Missed a radio show this week? '\
									'Please respond with the code for the corresponding ' \
									'show that you\'d like transcribed:\n' \
									'(1) Micro-finance Mondays \n' \
									'(2) Debt Management Tuesdays \n'
									'(3) Water Wednesdays: Irrigation \n' \
									'(4) Climate Resiliency Thursdays \n' \
									'(5) Community Fridays',
		                            to=_to
		                            )
		print(message.sid)

	elif body == '2': # hard coded
		message = client.messages.create(
		                            messaging_service_sid=messagingServiceSid,
		                            body='Debt Management Tuesday Transcription 15/03/2022\n\n' \
									'Hello everyone, and thanks for tuning into our ' \
									'Debt Management Tuesday show, with your hosts Arun and '\
									'Rakesh. Today we\'ll be covering topics related to micro-' \
									'financing for kisans, and we have on a special guest from ' \
									'the department of economics at The University of the Punjab, ' \
									'Dr. Maria Faiq Javaid...',
		                            to=_to
		                            )
		message = client.messages.create(
		                            messaging_service_sid=messagingServiceSid,
		                            body='Thank you for taking the time to connect. Could you respond '\
									'with some demographic information?\n'
									'e.g., reply with 1,4,5,8\n\n'\
									'Are you a...\n'
									'(1) Landowner or (2) Kisan\n'\
									'(3) Male or (4) Female\n'\
									'(5) Single or (6) Married or (7) Widowed\n'
									'(8) Received credit previously or (9) Have not received credit previously',
		                            to=_to
		                            )
		print(message.sid)
	elif body == '2,4,6,8': # hard coded response; responses will be recorded to db
		message = client.messages.create(
									messaging_service_sid=messagingServiceSid,
		                            body='धन्यवाद',
		                            to=_to
									)
		print(message.sid)
	else:
		message = client.messages.create(
									messaging_service_sid=messagingServiceSid,
									body='That was not a valid option. Please try again.',
									to=_to
									)
		print(message.sid)

	return("complete")

if __name__ == "__main__":
	app.run(debug=True)

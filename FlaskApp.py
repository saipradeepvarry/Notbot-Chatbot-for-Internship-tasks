// Install required Python Packages
flask

pip install flask
twilio

pip install twilio

from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse

app=Flask(__name__)
@app.route('/bot',methods=['POST'])
def bot():
    incoming_message=request.values.get('Body','').lower()
    sender_number = request.values.get('From', '')
    resp = MessagingResponse()
    msg = resp.message()
    if 'hi' in incoming_message:
        reply = 'Hi! Are you here to apply internship'
    elif 'Yes' or 'No':
        reply='Please Enter Your Name'
    elif incoming_message.isalpha():
        reply='Enter your email'
        if incoming_message.isalpha():
            reply="Please select how many years of experience you have with Python/JS/ Automation DevelopmentShow List: 1 year/n2years/n3 years/n4 years/n5 years"
    else:
        reply='Message: Thanks for connecting. We will getMessage: Thanks for connecting. We will get'
    
    msg.body(reply)
    print(incoming_message,reply)
    return str(resp)

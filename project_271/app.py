# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'Enter your account_sid here'
        auth_token = 'Enter your auth_token here'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('IS73bf9836bc6da5ef65d6e68fd12a6ede') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('https://collaborative-document.onrender.com/')



@app.route('/otp')
def get_otp():
   print("Processing...") 
   recieved_otp = request.form['received_otp']
   mobile_number = request.form['number']

    TWILIO_ACCOUNT_SID = 'AC8af15280d100a962aee20a95f541a905'
    TWILIO_SYNC_SERVICE_SID = 'IS73bf9836bc6da5ef65d6e68fd12a6ede'
    TWILIO_API_KEY = 'SKa3634b8fbae4d34d34802fa628a3276c'
    TWILIO_API_SECRET = 'W9U2UWS6olFetbGxFGnxljinMcoMOklr'

    verification_check = client.verify \
        .services('Enter your service ID') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

   if verification_check.status == "pending":
        return "Entered OTP is wrong"
    else:
        return redirect("https://collaborative-document.onrender.com/")

if __name__ == "__main__":
    app.run()


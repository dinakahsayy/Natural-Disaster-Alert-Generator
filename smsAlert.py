import sqlite3
from twilio.rest import Client
import os

def send_sms_alert(message):
     # Extract Twilio credentials from .env file
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
    MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

     # Check if phone numbers are set
    if MY_PHONE_NUMBER is None or TWILIO_PHONE_NUMBER is None:
        raise ValueError("Phone numbers must be set in the environment variables.")

    # Sending SMS using Twilio
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER
    )

    # Logging the alert to db
    log_alert(message)

def log_alert(message):
    conn = sqlite3.connect('alerts.db') 
    cursor = conn.cursor()

# Add alert into db
    cursor.execute('INSERT INTO alerts (message) VALUES (?)', (message,))

    conn.commit()
    conn.close()
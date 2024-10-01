from twitterMonitor import monitor_tweets
from tweetFilter import is_disaster_tweet
from smsAlert import send_sms_alert
import os
import schedule
import time
from database import create_database

# Creating the database and table
create_database()

# Print all env's for debugging
for key, value in os.environ.items():
     print(f"{key}: {value}")

# Extract Twilio credentials from .env file
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

# Define keywords to monitor on Twitter
keywords = "earthquake OR flood OR hurricane"

def job():
    try:
        print("Checking for disaster-related tweets...")
        tweets = monitor_tweets(keywords)

        if tweets:
            filtered_tweets = [tweet.full_text for tweet in tweets if is_disaster_tweet(
                tweet.full_text
            )]

            for tweet in filtered_tweets:
                send_sms_alert(f"Disaster Alert: {tweet}")
        else:
            print("No tweets found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    print("Checking for disaster-related tweets...")
    # Check tweets
    tweets = monitor_tweets(keywords)

    if tweets:
 # Filter relevant disaster-related tweets
        filtered_tweets = [tweet.full_text for tweet in tweets if is_disaster_tweet(tweet.full_text)]

 # Send SMS alerts for every relevant tweet found
        for tweet in filtered_tweets:
                send_sms_alert(f"Disaster Alert: {tweet}")
    else:
        print("No tweets found.")

# Schedule the time for the task to rerun
    schedule.every(10).minutes.do(job)

print("Scheduler started. Running job every 10 minutes.")

# Loop for scheduler
while True:
# Pending schedules
     schedule.run_pending()  
# Sleep for a bit
     time.sleep(1)
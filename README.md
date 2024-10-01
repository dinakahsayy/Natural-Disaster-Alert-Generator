# Natural-Disaster-Alert-Generator

The Natural Disaster Alert Generator is a Python application that monitors Twitter for disaster-related events and sends SMS alerts using Twilio. It provides real-time notifications about natural disasters to users so they can stay updated.

## Features
- **Twitter Monitoring**: Keeps an eye on tweets for disaster-related keywords.
- **Smart Filtering**: Only alerts you about tweets that really matter.
- **Instant SMS Alerts**: Get notified via SMS whenever a relevant tweet is detected.

## Technologies Used
- **Python**
- **Tweepy**
- **Twilio**
- **NLTK**
- **Poetry**

## Setup
If you want to clone this repository, make sure to create a .env file in the root directory of your project. 
Add the following lines, and add your actual keys and tokens:
TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_SECRET=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
MY_PHONE_NUMBER=

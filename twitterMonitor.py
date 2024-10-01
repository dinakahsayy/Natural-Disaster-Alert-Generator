import os
import tweepy

# Set up Twitter API authentication
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Debugging to see if API credentials show up
print(f"Twitter API Key: {TWITTER_API_KEY}") 
print(f"Twitter API Secret: {TWITTER_API_SECRET}")  

# Making sure all credentials are loading 
if not TWITTER_API_KEY or not TWITTER_API_SECRET:
    raise ValueError(
        "Twitter API credentials are not set. Please check your .env file."
    )

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

# Monitor tweets based on keywords
def monitor_tweets(keywords, count=10):
    try:
        tweets = api.search_tweets(
        q=keywords, lang='en', count=count, tweet_mode='extended'
        )
        return tweets
    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")
        return None
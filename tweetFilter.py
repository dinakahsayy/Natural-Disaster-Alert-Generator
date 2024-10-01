import nltk
from nltk.tokenize import word_tokenize

# Download needed NLTK data
nltk.download('punkt')

disaster_keywords = ["earthquake", "flood", "hurricane", "tsunami", "wildfire", "tornado", "landslide"]

# Checking if tweets have key words
def is_disaster_tweet(tweet_text):
    
# Tokenizing tweet and converting to lowercase
    tokens = word_tokenize(tweet_text.lower())  

# Checking if tokens have key words
    return any(word in tokens for word in disaster_keywords)

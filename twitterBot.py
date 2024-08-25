import tweepy # type: ignore

# Your Twitter API credentials
CLIENT_ID = 'BEspYIkKFqgynXMQOWchaHQ82'
CLIENT_SECRET = 'qJ0K6pvXLxBI8FDnNMoF6KsPi6Vrx5C9hxIJ181OeDJibpDYZL'
ACCESS_TOKEN = '1827553259328045056-n9JauPD0UWzCW3WWGMLlRPOmkRecbs'
ACCESS_TOKEN_SECRET = 'uAYZuxfiSMtMHZhTl9825xqwpMjc9WbddgmInxeDPaFj7'

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=CLIENT_ID, 
    consumer_secret=CLIENT_SECRET,
    access_token=ACCESS_TOKEN, 
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Post a tweet
tweet = "Hello World"
response = client.create_tweet(text=tweet)
print(f"https://twitter.com/user/status/{response.data['id']}")
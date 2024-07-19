#!/usr/bin/env python3
import tweepy # version > 4.12

#Create free account & project on https://developer.x.com

consumer_key = "API_KEY"
consumer_secret = "API_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_SECRET"

# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Upload image to Twitter. Replace 'filename' with your image filename.
# if you doesn't want to tweet with image, mute this line below
media_id = api.media_upload(filename="file.jpg").media_id_string

#TWEET
# if you doesn't want to tweet with image, use this line below
#response = client.create_tweet(text="text to twitter")
response = client.create_tweet(text="text to twitter",  media_ids=[media_id])

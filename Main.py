import tweepy
import json
import requests
from access_keys import *
from functions import *


API = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

response = Nasa_apod(nasa_key)

# picture = get_picture(response.json())
# tweet = response.json()["explanation"]

# print(tweet, picture)
#print(json.dumps(response.json(), indent=1))

# print(response.json()["explanation"])
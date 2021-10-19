import tweepy
import json
import requests
from access_keys import *

# print(API_key)

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)


# if api.verify_credentials() == False:
#     print("The user credentials are invalid.")
# else:
#     print("The user credentials are valid.")

request = "https://api.nasa.gov/planetary/apod?api_key="
response = requests.get(request + nasa_key)

# print(response.json())
print(json.dumps(response.json(), indent=1))

print(response.json()["explanation"])
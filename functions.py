import shutil
import requests
from pathlib import Path
import tweepy

def TwitterAPI(consumer_key, consumer_secret,access_token, access_token_secret):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	if api.verify_credentials() == False:
		print("The user credentials are invalid.")
		exit()
	else:
		print("The user credentials are valid.")

	return(api)


def Nasa_apod(nasaKey):
	request = "https://api.nasa.gov/planetary/apod?api_key="
	response = requests.get(request + nasaKey)

	if response.status_code == 200:
		print("Collected data from: ", request)
	else:
		print("Could not get data")
		exit()

	return(response)


def get_picture(response):
	url = response["hdurl"]
	filename =  url.split("/")[-1]
	path = Path("Images/" , filename)

	r = requests.get(url,stream = True)

	if r.status_code == 200:
		r.raw.decode_content = True

		with open (path,'wb') as f:
			shutil.copyfileobj(r.raw,f)

		print("Image has been successfully Downloaded: ",filename)
	else:
		print("image download failed")

	return(path)
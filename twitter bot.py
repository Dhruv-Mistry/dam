from twython import Twython
import os
import glob 

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)


message = "Hewo World"
twitter.update_status(status=message)
print("Tweeted: " + message)
imageFilenames = glob.glob('/home/pi/Desktop/Pictures/*')

newestImageFilename = max(imageFilenames,key=os.path.getctime)

message ="IntRuDEr DeTeCTed!"
with open(newestImageFilename,'rb') as photo:
    twitter.update_status_with_media(status=message,media=photo)

import json
import sys
import time
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy import API
from fun import *


# Scrapping Parameters
TrendingTopics = ["nba","Lebron James"]
AuthFilename = "auth.password"

# Launch the Stream
LauchScrapping(AuthFilename,TrendingTopics)
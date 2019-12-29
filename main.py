import json
import sys
import time
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy import API
from fun import *


# Scrapping Parameters
TrendingTopics = [
"retraites",
"réforme des retraites",
"reforme des retraites",
"reformedesretraites",
"grevistes",
"greviste",
"grève générale",
"greve generale",
"grevegenerale",
"retraite par point",
"retraites par point",
"retraiteparpoint",
"fiers de la grève",
"fiers de la greve",
"fiersdelagreve"
]
AuthFilename = "auth3.password"

# Launch the Stream
while True:
	
	try:
		LauchScrapping(AuthFilename,TrendingTopics)
	
	except KeyboardInterrupt as e:
		break
	
	except:
		continue
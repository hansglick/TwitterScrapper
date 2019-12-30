import json
import sys
import time
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy import API
from fun import *


# Scrapping Parameters
TrendingTopics =["racisme",
"racism",
"raciste",
"insécurité",
"immigration",
"intersectionnalité",
"intersectionnalite",
"lutte intersectionnelle",
"afroféminisme",
"afro féminisme",
"afrofeminisme",
"afro feminisme",
"fachosphere",
"appropriation culturelle",
"fragilité blanche",
"privilège blanc",
"privilege blanc",
"white privilege",
"white fragility",
"fachosphère",
"islamisme",
"islamiste",
"islamique",
"white supremaciste",
"suprémaciste blanc",
"suprémacisme blanc",
"supremaciste blanc",
"supremacisme blanc",
"white supremacist",
"white supremacism",
"islamo-gauchiste",
"islamogauchiste",
"islamogauchisme",
"islamo-gauchisme",
"islamo gauchiste",
"islamo gauchistes",
"islamo gauchisme",
"radical",
"islamophobie",
"islamophobe",
"antisémitisme",
"antiblanc",
"anti-blanc",
"sionisme",
"sioniste",
"antisioniste",
"antisionisme",
"attentat"]
AuthFilename = "auth.password"

# Launch the Stream
while True:
	
	try:
		LauchScrapping(AuthFilename,TrendingTopics)
	
	except KeyboardInterrupt as e:
		break
	
	except:
		continue
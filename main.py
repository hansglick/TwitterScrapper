import json
import sys
import time
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy import API
from fun import *


# Scrapping Parameters
TrendingTopics =["racisme",
"insécurité",
"immigration",
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
LauchScrapping(AuthFilename,TrendingTopics)
import json
import sys
import time
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from tweepy import API
from fun import *


# Scrapping Parameters
TrendingTopics = ["racisme",
"insécurité",
"appropriation culturelle",
"fragilité blanche",
"privilège blanc",
"white fragility",
"white privilege"
"immigration",
"fachosphère",
"fachosphere",
"islamisme",
"islamiste",
"radical",
"islamophobie",
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
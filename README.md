# Twitter Scraper

### En bref
Cette application permet de scrapper Twitter en temps réel via la Twitter Stream API. En bref, on passe en input des mots clés qui permettent de filtrer les tweets à récupérer.

### Cloner l'environnement
Afin de reproduire l'environnement nécessaire à faire tourner l'application :
```
conda env create -f TwitterScraperEnv.yml
conda activate twitter
```

### Renseigner le login et le password
L'application prend en input un fichier `auth.password` que l'utilisateur doit créer lui-même. La structure de celui-ci est la suivante :
```
consumer_token
consumer_secret
access_token
access_token_secret
```


### Renseigner l'input
Pour renseigner les mots-clés permettant de filtrer les tweets à récupérer, ouvrir le fichier `main.py` et modifier la liste `TrendingTopics`, par exemple : 
```
TrendingTopics = ["nba","playoffs","Lebron"]
```

import requests
import json

endpoint_url = 	'https://api.spotify.com/v1/recommendations'
access_token = 'BQCsVf53VO7ZhxTEySC5IthvzDK0LAcvoZYZpV6rbzEHwMuQQ7TkxkmU5wX378QpsHKGbePTaWRcx0R4xzIDlT5TgvqpTmofP4_MrHDEJmUxqiUGZuqdHp_CFmiL7Y2JQltZ15TqVIzbkePG-DfrS-NJBvFgCl_HZP6DDREYfGdgs_OL'

#FILTERS
limit = 10 #Number of songs in playlist
market = 'AU' #Country
seed_genres = "heavy_metal" #Genres 
target_danceability = 0.2
seed_artist = 'https://open.spotify.com/artist/3OpqU68JpZlzvjAJj3B2Da?si=5BpK2SFmQKGhxsdZR9nCHw'



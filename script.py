import requests
import json

endpoint_url = "https://api.spotify.com/v1/recommendations?"
access_token = "ENTER_ACCESS_TOKEN_HERE"

# OUR FILTERS
limit: int = 10
seed_genres: str = "pop"
market: str = "AU"

query: str = f"{endpoint_url}?limit={limit}&seed_genres={seed_genres}&market={market}"
response = requests.get(query, headers={"Content-Type": "application/json", "Authorization":f"Bearer {access_token}"})

uris: [] = []
for (i,j) in enumerate(response.json()["tracks"]):
    uris.append(j["uri"])
    print(f"{i+1})  \"{j['name']}\" by {j['artists'][0]['name']}")





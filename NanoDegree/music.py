import requests

url = "https://shazam.p.rapidapi.com/songs/list-artist-top-tracks"

querystring = {"id":"40008598","locale":"en-US"}

headers = {
    'x-rapidapi-host': "shazam.p.rapidapi.com",
    'x-rapidapi-key': "f0e9484262mshfd3c258499e71b9p109e6djsnf8c3614c3590"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

tracks = response.json()['tracks']
for track in tracks:
    print(track['title'])
    print(track['share']['href'])
    print(track['share']['image'])
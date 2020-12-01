import requests
import json
from refresh import Refresh
from random import randint
from time import sleep


token = Refresh().refresh()

def play_playlist():

    query = "https://api.spotify.com/v1/me/player/play?device_id=52c39de05bdc3823b15b0ff3187bd13ee92257fb"

    position = randint(0, get_playlist_number() - 3)

    request_body = json.dumps({"context_uri": "spotify:playlist:5xToaLxyFVTuyh6m1wheip",
    "offset": {"position": position},
    "position_ms": 20})

    requests.put(query,
        data = request_body,
        headers = {"Authorization":f"Bearer {token}"})

def get_playlist_number():

    query = f"https://api.spotify.com/v1/playlists/5xToaLxyFVTuyh6m1wheip"

    response = requests.get(query,
        headers = {"Authorization":f"Bearer {token}"})
    
    response_json = response.json()

    s = 0
    for i in response_json["tracks"]["items"]:
        s += 1

    return int(s)

def volume(vp):

    query = f"https://api.spotify.com/v1/me/player/volume?volume_percent={vp}"

    response = requests.put(query,
        headers = {"Authorization": f"Bearer {token}"})

def skip_next():

    query = "https://api.spotify.com/v1/me/player/next"

    requests.post(query,
        headers = {"Authorization": f"Bearer {token}"})    

def skip_previous():

    query = "https://api.spotify.com/v1/me/player/previous"

    requests.post(query,
        headers = {"Authorization": f"Bearer {token}"})

def pause():

    query = " https://api.spotify.com/v1/me/player/pause"

    requests.put(query,
        headers = {"Authorization": f"Bearer {token}"})

def resume():

    query = "https://api.spotify.com/v1/me/player/play"

    requests.put(query,
        headers = {"Authorization": f"Bearer {token}"})

def currently_playing():

    query = "https://api.spotify.com/v1/me/player/currently-playing"

    response = requests.get(query,
        headers = {"Authorization": f"Bearer {token}"})

    response_json = response.json()

    return response_json

def devices():

    query = "https://api.spotify.com/v1/me/player/devices"

    response = requests.get(query,
        headers = {"Authorization": f"Bearer {token}"})

    response_json = response.json()

    print(response_json)

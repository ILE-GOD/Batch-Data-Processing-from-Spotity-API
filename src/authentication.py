# import os, json, requests
# from dotenv import load_dotenv

# load_dotenv()

# def get_token(client_id, client_secret):
#     url = "https://accounts.spotify.com/api/token"
#     payload = {
#         "grant_type": "client_credentials",
#         "client_id": client_id,
#         "client_secret": client_secret
#     }

#     response = requests.post(url, data=payload)
#     response.raise_for_status()
#     return response.json()

import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_token():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    if not client_id or not client_secret:
        raise ValueError("Missing SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET")

    url = "https://accounts.spotify.com/api/token"

    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=payload, timeout=10)
    response.raise_for_status()

    return response.json()["access_token"]

# import requests
# import time
# import os
# from authentication import get_token


# BASE_URL = "https://api.spotify.com/v1"


# def _get_headers(token):
#     return {
#         "Authorization": f"Bearer {token['access_token']}"
#     }


# def _safe_get(url, token, params=None):
#     """
#     Makes a request and refreshes token automatically if expired.
#     """
#     headers = _get_headers(token)
#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 401:
#         # token expired → refresh
#         token.update(get_token(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET")))
#         headers = _get_headers(token)
#         response = requests.get(url, headers=headers, params=params)

#     response.raise_for_status()
#     return response.json()


# def get_paginated_new_releases(token, limit=20):
#     """
#     Fetch all new release albums using pagination.
#     """
#     url = f"{BASE_URL}/browse/new-releases"
#     params = {"limit": limit, "offset": 0}

#     all_albums = []

#     while True:
#         data = _safe_get(url, token, params=params)
#         albums = data["albums"]["items"]
#         all_albums.extend(albums)

#         if data["albums"]["next"] is None:
#             break

#         params["offset"] += limit
#         time.sleep(0.2)

#     return all_albums


# def get_paginated_album_tracks(album_id, token, limit=20):
#     """
#     Fetch all tracks for a single album using pagination.
#     """
#     url = f"{BASE_URL}/albums/{album_id}/tracks"
#     params = {"limit": limit, "offset": 0}

#     all_tracks = []

#     while True:
#         data = _safe_get(url, token, params=params)
#         tracks = data["items"]
#         all_tracks.extend(tracks)

#         if data["next"] is None:
#             break

#         params["offset"] += limit
#         time.sleep(0.2)

#     return all_tracks


import requests
import time

BASE_URL = "https://api.spotify.com/v1"


def _get_headers(token: str):
    return {"Authorization": f"Bearer {token}"}


def _safe_get(url, token, params=None):
    headers = _get_headers(token)
    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def get_paginated_new_releases(token, limit=20):
    url = f"{BASE_URL}/browse/new-releases"
    params = {"limit": limit, "offset": 0}

    all_albums = []

    while True:
        data = _safe_get(url, token, params=params)
        albums = data["albums"]["items"]
        all_albums.extend(albums)

        if data["albums"]["next"] is None:
            break

        params["offset"] += limit
        time.sleep(0.2)

    return all_albums


def get_paginated_album_tracks(album_id, token, limit=20):
    url = f"{BASE_URL}/albums/{album_id}/tracks"
    params = {"limit": limit, "offset": 0}

    all_tracks = []

    while True:
        data = _safe_get(url, token, params=params)
        tracks = data["items"]
        all_tracks.extend(tracks)

        if data["next"] is None:
            break

        params["offset"] += limit
        time.sleep(0.2)

    return all_tracks

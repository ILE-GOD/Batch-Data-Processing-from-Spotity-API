# from authentication import get_token
# from endpoint import get_paginated_new_releases, get_paginated_album_tracks
# import os, json, datetime

# def main():
#     token = get_token(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))

#     albums = get_paginated_new_releases(token)

#     album_items = {}

#     for album in albums:
#         album_id = album["id"]
#         tracks = get_paginated_album_tracks(album_id, token)
#         album_items[album_id] = tracks

#     ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

#     with open(f"src/output/album_items_{ts}.json", "w") as f:
#         json.dump(album_items, f, indent=2)

# if __name__ == "__main__":
#     main()


from authentication import get_token
from endpoint import get_paginated_new_releases, get_paginated_album_tracks
import json
import datetime
import os


def main():
    token = get_token()

    albums = get_paginated_new_releases(token)

    album_items = {}

    for album in albums:
        album_id = album["id"]
        tracks = get_paginated_album_tracks(album_id, token)
        album_items[album_id] = tracks

    os.makedirs("src/output", exist_ok=True)

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    with open(f"src/output/album_items_{ts}.json", "w") as f:
        json.dump(album_items, f, indent=2)

    print("✅ Batch extraction complete")


if __name__ == "__main__":
    main()


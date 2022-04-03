#!/bin/env python3

from io import BytesIO
import json
import os
import requests
import sys
from PIL import Image

artwork_dir = "../artwork/"

# Fetch JSON fname
if len(sys.argv) < 2:
    print("Must provide at least one JSON file as argument")
    sys.exit()
JSON_fname = sys.argv[1]
if not os.path.exists(JSON_fname):
    print("{} does not exist}")
    sys.exit()

# Load sources metadata from JSON
with open(JSON_fname) as f:
    build_data = json.load(f)

# Load artworks paths
artworks = []
for group in build_data["artwork_groups"]:
    fpath = os.path.join(artwork_dir, "{}/positions.json".format(group))
    with open(fpath) as f:
        images_data = json.load(f)
    for data in images_data:
        data["img_url"] = os.path.join(artwork_dir, group, data["img_url"])
        artworks.append(data)

# Reverse artworks so higher up on the list get written last (so are on top)
artworks.reverse()

# Create new empty transparent image
overlay_img = Image.new(
    "RGBA",
    (build_data["width"], build_data["height"]),
    (0, 0, 0, 0)
)

# Load source images and paste each into overlay at location
for data in artworks:

    if os.path.exists(data["img_url"]):

        print(data["img_url"])
        img = Image.open(data["img_url"])

    elif "http://" in data["img_url"] or "https://" in data["img_url"]:

        print("Fetching {} ...".format(data["img_url"],))
        try:
            response = requests.get(data["img_url"], headers={'Cache-Control': 'no-cache'})
        except:
            continue

        img = Image.open(BytesIO(response.content))
    
    else:

        print("No local image or valid URL")
        sys.exit()

    overlay_img.paste(img, (data["x0"], data["y0"]))

# Save raw overlay
overlay_img.save(build_data["output_fname"], quality=95)
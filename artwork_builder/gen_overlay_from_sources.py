#!/bin/env python3

from io import BytesIO
import json
import os
import requests
from PIL import Image

# Load sources metadata from JSON
# The list if reversed so artworks higher up get written last

with open("artwork_sources.json") as f:
    sources_data = json.load(f)
sources_data.reverse()

# Create new empty transparent image

overlay_width = 1000
# overlay_width = 2000
overlay_height = 1000

overlay_img = Image.new("RGBA", (overlay_width, overlay_height), (0, 0, 0, 0))

# Load source images and paste each into overlay at location

for data in sources_data:

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

    overlay_img.paste(img, (data["x0"], data["y0"]))

# Save raw overlay
overlay_img.save("overlay_test.png", quality=95)
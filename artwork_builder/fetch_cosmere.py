#!/bin/env python3

from io import BytesIO
import requests
from PIL import Image
import matplotlib.pyplot as plt
import numpy

cosmere_overlay_url = "https://raw.githubusercontent.com/Atkion/placeCosmereOverlay/master/template.png"

print("Fetching {} ...".format(cosmere_overlay_url))
response = requests.get(cosmere_overlay_url, headers={'Cache-Control': 'no-cache'})
img = Image.open(BytesIO(response.content))

data = numpy.array(img)
new_data = data[1::3,1::3,:].copy(order='C')

plt.imsave("../artwork/allies/cosmere.png", new_data, dpi=100, format="png")


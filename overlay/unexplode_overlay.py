#!/bin/env python3

import matplotlib.pyplot as plt
import numpy

overlay = plt.imread("tuxoverlay.png")

raw = overlay[1::3,1::3,:]

plt.imsave("overlay_raw.png", raw, dpi=100, format="png")
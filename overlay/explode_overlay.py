#!/bin/env python3

import matplotlib.pyplot as plt
import numpy
import os

try:
    os.mkdir("out")
except FileExistsError:
    pass

raw = plt.imread("overlay_raw.png")

overlay = numpy.zeros((len(raw) * 3, len(raw[0]) * 3, 4), dtype=numpy.float32)

overlay[1::3, 1::3, :] = raw

plt.imsave("out/overlay.png", overlay, dpi=100, format="png")

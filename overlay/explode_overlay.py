#!/bin/env python3

import matplotlib.pyplot as plt
import numpy
import os

try:
    os.mkdir("out")
except FileExistsError:
    pass

p = plt.imread("overlay_raw.png")

newImage = numpy.zeros((len(p) * 3, len(p[0]) * 3, 4), dtype=numpy.float32)


# convert a point on the true image to a point on the exploded image
def fix_pos(pos):
    return pos * 3 + 1


for row in range(len(p)):
    for tile in range(len(p[row])):
        for i in range(len(p[row][tile])):
            newImage[fix_pos(row)][fix_pos(tile)][i] = p[row][tile][i]

plt.imsave("out/overlay.png", newImage, dpi=100, format="png")

#!/bin/env python3

import matplotlib.pyplot as plt
import numpy

p = plt.imread("tuxoverlay.png")

newImage = numpy.zeros((len(p) // 3, len(p[0]) // 3, 4), dtype=numpy.float32)


# convert a point on the exploded image to a point on the true image
def fix_pos(pos):
    return (pos - 1) // 3


for row in range(len(p)):
    if not ((row - 1) % 3):
        for tile in range(len(p[row])):
            if not ((tile - 1) % 3):
                for i in range(len(p[row][tile])):
                    newImage[fix_pos(row)][fix_pos(tile)][i] = p[row][tile][i]

plt.imsave("overlay_raw.png", newImage, dpi=100, format="png")

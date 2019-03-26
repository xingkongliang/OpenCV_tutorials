#! /usr/bin/env python
# -*- coding:utf8 -*-
# __author__ : "ZhangTianliang"
# Date: 1/15/18

import numpy as np
import cv2 as cv

# load an color image in grayscale

print(cv.__version__)
img = cv.imread('data/messi5.jpg', 0)


# Display an image
cv.imshow('image', img)

k = cv.waitKey(0)

if k == 27:             # wait for ESC key to exit
    cv.destroyWindow()
    print('press ESC')
elif k == ord('s'):     # wait for 's' key to save and exit
    # Write an image
    cv.imwrite('messigray.png', img)
    cv.destroyWindow()


# Using Matplotlib
from matplotlib import pyplot as plt

print('Using Matplotlib.')

img = cv.imread('data/messi5.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img, interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# img = cv.imread('data/messi5.jpg', 0)
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()


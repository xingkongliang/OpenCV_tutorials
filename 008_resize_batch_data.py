#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : "ZhangTianliang"
# Date: 18-8-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import numpy as np
import cv2 as cv

import skimage
from skimage import io


# moon = io.imread('data/messi5.jpg')
# print("moon shape: ", moon.shape)
# print("moon max: ", moon.max())

print("opencv version: ", cv.__version__)
img = cv.imread('data/messi5.jpg')
print("image opencv shape: ", img.shape)
img = img.transpose((2, 0, 1))
print("image shape: ", img.shape)

# input_imgs is your input
input_imgs = np.concatenate((img[np.newaxis, ...], img[np.newaxis, ...], img[np.newaxis, ...], img[np.newaxis, ...]), axis=0)
print("input_imgs shape: ", input_imgs.shape)

imgs_trans = input_imgs.transpose((0, 2, 3, 1))

print("img_trans shape: ", imgs_trans.shape)
target_h, target_w = img.shape[1]*2, img.shape[2]*2

img_out = np.zeros((input_imgs.shape[0], target_h, target_w, input_imgs.shape[1]))

for i, img in enumerate(imgs_trans):
    img_resized = cv.resize(img, (target_w, target_h), interpolation=cv.INTER_CUBIC)
    img_out[i, ...] = img_resized

img_out = img_out.transpose((0, 3, 1, 2))
print("img_out shape: ", img_out.shape)
print("img_out max: ", img_out.max())


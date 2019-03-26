#! /usr/bin/env python
# -*- coding:utf8 -*-
# __author__ : "ZhangTianliang"
# Date: 1/15/18

import numpy as np
import cv2

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))
print(x + y)          # 250+10=260 % 256 = 4

# Image Blending
img1 = cv2.imread('data/pic1.png')
img2 = cv2.imread('data/pic2.png')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()





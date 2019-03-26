#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : "ZhangTianliang"
# Date: 18-9-16

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import cv2
print(cv2.__version__)
print(cv2.__file__)
img = cv2.imread('data/messi5.jpg', 0)
height = img.shape[0]
width = img.shape[1]

fps = 16
size = (width, height)

# v = cv2.VideoWriter("a.avi",cv2.VideoWriter_fourcc('M','J','P','G'),fps,size)
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# v = cv2.VideoWriter("a.avi", fourcc, fps, size)
#
# for i in range(200):
#     v.write(img)

# Define the codec and create VideoWriter object
# out = cv2.VideoWriter('oto_other.avi', -1, fps, size)
##fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# out = cv2.VideoWriter('output.mp4', fourcc, fps, size, False)
out = cv2.VideoWriter('lianzheng.avi', fourcc, 20.0, (640, 480))

for i in range(200):
    # write the flipped frame
    out.write(img)

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
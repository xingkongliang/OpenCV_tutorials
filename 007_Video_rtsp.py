#! /usr/bin/env python
# -*- coding:utf8 -*-
# __author__ : "ZhangTianliang"
# Date: 2018/1/30

import cv2
import os

print('cv2.__file__: ', cv2.__file__)
print('opencv version: ', cv2.__version__)

# os.system('ls -al /root/Util/miniconda/lib/python2.7/site-packages/cv2.so')

cap = cv2.VideoCapture("rtsp://admin:123456@124.16.71.158:554/11")
# cap = cv2.VideoCapture("rtsp://admin:123456@localhost:554/11")

print cap.isOpened()

if False == cap.isOpened():
    print('open video failed')
else:
    print('open video succeeded')

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    cv2.waitKey(1)

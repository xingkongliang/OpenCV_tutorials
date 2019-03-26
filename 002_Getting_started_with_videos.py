#! /usr/bin/env python
# -*- coding:utf8 -*-
# __author__ : "ZhangTianliang"
# Date: 1/15/18

import numpy as np
import cv2
import os
file = 'data/768x576.avi'
#file = 'liguo.mp4'
if os.path.exists(file):
    print('file exists.')
else:
    print('file not exists.')


cap = cv2.VideoCapture(file)

print('cv2.__file__: ', cv2.__file__)
print('opencv version: ', cv2.__version__)

# os.system('ls -al /root/Util/miniconda/lib/python2.7/site-packages/cv2.so')


if cap.isOpened():
    print('cap is opened!')
else:
    print('cap fail!')

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the reuslting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everthing done, release the capture
cap.release()
cv2.destroyAllWindows()

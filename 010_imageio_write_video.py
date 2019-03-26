#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : "ZhangTianliang"
# Date: 18-9-16

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import imageio
import cv2
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

img_dir = '/media/tianliang/Projects/Caffe2_Projects/MDetectron-v4/test/coco_caltech_test/generalized_rcnn/vis'
mask_dir = '/media/tianliang/Projects/Caffe2_Projects/detectron-output/' \
           'caltech_1gpu_e2e_faster_rcnn_R-50-FPN_v7_01/test_output_mask'

fps = 16
writer = imageio.get_writer('Pedestrian_Detection_608x800_part2.mp4', fps=fps)

images_files = sorted(glob.glob("{}/*.jpg".format(img_dir)))

for i in range(6000, len(images_files)):
    image_file = images_files[i]
    basename = image_file.split('/')[-1]
    mask_file = os.path.join(mask_dir, "{}_mask.png".format(basename.split('.')[0]))
    assert os.path.exists(image_file)
    assert os.path.exists(mask_file)

    img = cv2.imread(image_file)
    mask = cv2.imread(mask_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

    img_h = img.shape[0]
    img_w = img.shape[1]

    mask_h = mask.shape[0]
    mask_w = mask.shape[1]

    outsize_h = mask_h
    outsize_w = mask_w

    img_target = cv2.resize(img, (outsize_w, outsize_h), interpolation=cv2.INTER_CUBIC)
    mask_target = cv2.resize(mask, (outsize_w, outsize_h), interpolation=cv2.INTER_CUBIC)

    assert mask_target.shape == img_target.shape

    out = np.zeros((outsize_h, outsize_w*2+50, 3))

    out[:, 0:outsize_w, :] = img_target
    out[:, outsize_w+50:outsize_w*2+50, :] = mask_target

    # plt.imshow(out)
    # plt.show()
    writer.append_data(out.astype(np.uint8))
    # if i == 6000:
    #     break
    print("{}---{}".format(i, len(images_files)))
writer.close()
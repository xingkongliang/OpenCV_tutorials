#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ : "ZhangTianliang"
# Date: 18-9-16

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

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

img_dir = 'best_mask'

images_files = sorted(glob.glob("{}/*.png".format(img_dir)))

image_file = images_files[0]

img = cv2.imread(image_file)

src_h = img.shape[0]
src_w = img.shape[1]
out = np.zeros((src_h * 2, src_w * 3, 3))

for i in range(0, len(images_files)):
    image_file = images_files[i]
    basename = image_file.split('/')[-1]

    img = cv2.imread(image_file)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_h = img.shape[0]
    img_w = img.shape[1]

    assert img_h == src_h
    assert img_w == src_w

    # img_target = cv2.resize(img, (outsize_w, outsize_h), interpolation=cv2.INTER_CUBIC)
    print(int((i/3))*src_h, int((i/3 + 1))*src_h)
    print((i%3)*src_w, (i%3 + 1)*src_w)
    out[int((i/3))*src_h:int((i/3 + 1))*src_h, (i%3)*src_w:(i%3 + 1)*src_w, :] = img
cv2.imwrite(os.path.join(img_dir, 'out.png'), out.astype(np.uint8))
# plt.imshow(out.astype(np.uint8))
# plt.show()


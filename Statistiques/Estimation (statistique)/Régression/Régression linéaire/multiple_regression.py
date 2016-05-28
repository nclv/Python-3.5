# -*- coding: utf-8 -*-

import os

import numpy as np

height = [1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63,
          1.65, 1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83]
weight = [52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93,
          61.29, 63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46]

X = np.mat(height**np.arange(3)[:, None])
y = np.mat(weight)

print(y * X.T * (X * X.T).I)

X = np.array(height)[:, None]**range(3)
y = weight

print(np.linalg.lstsq(X, y)[0])

os.system("pause")

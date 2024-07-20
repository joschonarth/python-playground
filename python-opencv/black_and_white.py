import numpy as np
import cv2

img = cv2.imread("img/dog.jpg", 0)
# cv2.imwrite("dog_bw.jpg", img)

from matplotlib import pyplot as plt
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
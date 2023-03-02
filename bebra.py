import numpy as np
import cv2 as cv
img = cv.imread('/home/it-7/Levchill/spider.jpeg')
img = img[100: int(img.shape[0]-200), 200:int(img.shape[1]-300)]
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
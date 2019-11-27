import numpy as np
import cv2

img = cv2.imread("j.jpg")

img1 = cv2.flip(img,1)  #镜像
img2 = cv2.flip(img,1)


cv2.imshow('dst',img1)
cv2.imshow("source", img)
cv2.imshow('dst',img2)

cv2.waitKey(0)
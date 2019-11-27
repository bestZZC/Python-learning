
import numpy as np
from imutils import contours
import cv2


img= cv2.imread('red1.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, 3, (0,255,0), 3)
x,y,w,h = cv2.boundingRect(cnt)
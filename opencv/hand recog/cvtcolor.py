import cv2


img1 = cv2.imread("3.jpg")
img_ret2 = cv2.cvtColor(img1,cv2.COLOR_BGRA2BGR)
img_ret = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
img_ret1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.namedWindow("source",0)
cv2.resizeWindow("source",400,400)

cv2.imshow('source',img1)
cv2.namedWindow("BGRcolor",0)
cv2.resizeWindow("BGRcolor",400,400)
cv2.imshow('BGRcolor',img_ret2)
cv2.namedWindow("HSV",0)
cv2.resizeWindow("HSV",400,400)
cv2.imshow('HSV',img_ret)
cv2.namedWindow("GRAY",0)
cv2.resizeWindow("GRAY",400,400)
cv2.imshow('GRAY',img_ret1)
cv2.waitKey(0)
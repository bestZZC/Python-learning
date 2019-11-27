import cv2 as cv

print("welcome")

src=cv.imread("b.jpeg",0)
gray = cv.cvtColor(src ,cv.COLOR_RGB2BGR)
gray = cv.cvtColor(gray,cv.COLOR_BGR2GRAY)
cv.namedWindow("input image",0)
cv.imshow("input image", src)

cv.waitKey(0)
cv.destroyWindow("input image")
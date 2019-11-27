from imutils import paths
import numpy as np
import imutils
import cv2



def find_marker(image):
    #convert img to grayscale,边缘处理
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    #gray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(img, (5, 5), 0)
    edged = cv2.Canny(gray, 35, 125)
    cv2.imshow("red", edged)

    #largest edge
    cnts = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts , key=cv2.contourArea)

    return cv2.minAreaRect(c)
def distance(knownWidth,focalLength,perWidth):
    return (knownWidth *focalLength)/perWidth
#initialize
KNOWN_DISTANCE = 33.0

KNOWN_WIDTH = 11.0

img = cv2.imread("red1.jpg", 0)
marker =find_marker(img)
focalLengh =(marker[1][0] *  KNOWN_DISTANCE)/ KNOWN_WIDTH


measure_img=cv2.imread("red1.jpg")
marker = find_marker(measure_img)
inches =distance(KNOWN_WIDTH,focalLengh,marker[1][0])

box = cv2.boxPoints(marker) if    imutils.is_cv2() else cv2.boxPoints(marker)
box =np.int0(box)
cv2.drawContours(measure_img,[box],-1,(0,255,0),2)
cv2.putText(measure_img,"%.2fm" % (inches / 12),
            (measure_img.shape[1] - 200, measure_img.shape[0] - 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            2.0, (0, 255, 0), 3)

cv2.imshow("distance",measure_img)





cv2.waitKey(0)




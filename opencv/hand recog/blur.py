import cv2

imgName = "j.jpg";
kernel_size = (9, 9);
sigma = 1.5;

img = cv2.imread(imgName);
img1= cv2.medianBlur(img, 9)
img2 = cv2.GaussianBlur(img, kernel_size, sigma);


cv2.imshow("source",img)
cv2.imshow("medianBlur",img1)
cv2.imshow("GaussianBlur",img2)
cv2.waitKey(0)


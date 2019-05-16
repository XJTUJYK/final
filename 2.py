import cv2
import numpy as np

test = cv2.imread("./test6.jpg")
test_g = cv2.GaussianBlur(test, (3, 3), 0)
gray = cv2.cvtColor(test_g, cv2.COLOR_BGR2GRAY)

test_canny = cv2.Canny(gray, 50, 150)
test_sobelx = cv2.Sobel(gray, cv2.CV_16S, 1, 0)
test_sobely = cv2.Sobel(gray, cv2.CV_16S, 0, 1)

abs_test_sobelx = cv2.convertScaleAbs(test_sobelx)
abs_test_sobely = cv2.convertScaleAbs(test_sobely)
sobel_dst = cv2.addWeighted(abs_test_sobelx, 0.5, abs_test_sobely, 0.5, 0)

img = test.copy()
lines = cv2.HoughLines(test_canny, 1, np.pi/180, 80)
#lines = cv2.HoughLines(sobel_dst, 1, np.pi/180, 750)
#lines = cv2.HoughLines(abs_test_laplacian, 1, np.pi/180, 650)
for i in range(0, lines.shape[0]):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('houghlines', img)
#cv2.imwrite('test3_houghlines_sobel.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
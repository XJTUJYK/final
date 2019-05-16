import cv2

test = cv2.imread("C:\\Users\\lenovo\\Desktop\\New folder (3)\\test4.bmp", 0)

test_g = cv2.GaussianBlur(test, (3, 3), 0)
test_canny = cv2.Canny(test_g, 50, 150)
test_laplacian = cv2.Laplacian(test, cv2.CV_16S, ksize=3)
test_sobelx = cv2.Sobel(test, cv2.CV_16S, 1, 0)
test_sobely = cv2.Sobel(test, cv2.CV_16S, 0, 1)

abs_test_laplacian = cv2.convertScaleAbs(test_laplacian)
abs_test_sobelx = cv2.convertScaleAbs(test_sobelx)
abs_test_sobely = cv2.convertScaleAbs(test_sobely)
sobel_dst = cv2.addWeighted(abs_test_sobelx, 0.5, abs_test_sobely, 0.5, 0)

cv2.imshow('test_canny', test_canny)
cv2.imshow('test_laplacian', abs_test_laplacian)
cv2.imshow('sobel', sobel_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
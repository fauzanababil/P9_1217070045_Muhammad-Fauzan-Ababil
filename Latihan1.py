import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('daun.jpg',0)
laplacian64f = cv.Laplacian(img,cv.CV_64F)
abs_laplacian64f = np.absolute (laplacian64f)
laplacian_8u = np.uint8(abs_laplacian64f)
sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
abs_sobelx64f = np.absolute(sobelx64f)
sobelx_8u= np.uint8(abs_sobelx64f)
sobely64f= cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
abs_sobely64f =np.absolute(sobely64f)
sobely_8u= np.uint8(abs_sobely64f)
magnitudesobel = cv.magnitude (sobelx64f, sobely64f)
abs_sobel64f = np.absolute (magnitudesobel)
sobel_8u= np.uint8(abs_sobel64f)

plt.subplot(3,2,1), plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,2), plt.imshow(laplacian_8u,cmap = 'gray')
plt.title('Laplacian'), plt.xticks ([]), plt.yticks([])
plt.subplot(3,2,3), plt.imshow(sobelx_8u, cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,4), plt.imshow(sobely_8u,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,5), plt.imshow(sobel_8u, cmap = 'gray')
plt.title('Sobel Magnitude'), plt.xticks ([]), plt.yticks([])
plt.show()
cv.imshow('Original', img)
cv.imshow('Laplacian', laplacian_8u)
cv.imshow("Sobel X', sobelx_8u")
cv.imshow("Sobel Y', sobely_8u")
cv.imshow('Sobel Magnitude', sobel_8u)
cv.waitKey(0)
cv.destroyAllWindows()
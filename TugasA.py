import cv2
import numpy as np

def sobel_detection(image):
  """
  Fungsi untuk deteksi tepi menggunakan operator Sobel.

  Args:
    image: Matriks NumPy yang berisi gambar.

  Returns:
    Hasil deteksi tepi (matriks NumPy).
  """
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0)
  sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1)
  sobel_magnitude = np.sqrt(sobel_x*2 + sobel_y*2)
  sobel_magnitude = sobel_magnitude / np.max(sobel_magnitude)
  return sobel_magnitude

def laplacian_detection(image):
  """
  Fungsi untuk deteksi tepi menggunakan operator Laplacian.

  Args:
    image: Matriks NumPy yang berisi gambar.

  Returns:
    Hasil deteksi tepi (matriks NumPy).
  """
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
  laplacian = laplacian / np.max(laplacian)
  return laplacian

def canny_detection(image):
  """
  Fungsi untuk deteksi tepi menggunakan Canny edge detection.

  Args:
    image: Matriks NumPy yang berisi gambar.

  Returns:
    Hasil deteksi tepi (matriks NumPy).
  """
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray_image, 50, 150)
  return edges


image = cv2.imread('daun.jpg')
sobel_magnitude = sobel_detection(image)
laplacian = laplacian_detection(image)
canny_edges = canny_detection(image)

cv2.imshow('Sobel', sobel_magnitude)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny_edges)
cv2.waitKey(0)
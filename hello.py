import cv2 as cv


img = cv.imread('cvphoto/mycat.jpeg')
cv.imshow('mycat', img)

img1 = cv.imread('cvphoto/mydog.jpg')
cv.imshow('mydog', img1)


cv.waitKey()
          
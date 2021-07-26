import cv2
import matplotlib.pyplot as plt

#display the image
image = cv2.imread("deer.jpg")
cv2.imshow("Deer",image)
cv2.waitKey(0)

#convert into black and white image
grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("New Deer",grey)
cv2.waitKey(0)

#invert the black and white image
inverted_image = 255 - grey
cv2.imshow("Inverted", inverted_image)
cv2.waitKey(0)

#blur the inverted image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
cv2.imshow("Blur", blurred)
cv2.waitKey(0)

#invert the blurred image
inverted_blurred = 255 - blurred

#divide the grey image by the new inverted blurred image
pencil_sketch = cv2.divide(grey, inverted_blurred, scale=256.0)
cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

#visualize both original ad new image together
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)


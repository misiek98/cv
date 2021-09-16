import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\bear.jpg')
cv2.imshow('image', img)
cv2.waitKey(delay=0)  # delay w milisekundach. 1000 to 1 sekunda

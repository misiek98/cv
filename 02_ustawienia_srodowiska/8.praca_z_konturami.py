import cv2

original_img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\python.png')
img = original_img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


thresh = cv2.threshold(gray, thresh=250, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]

img_cnt = cv2.drawContours(image=img.copy(), contours=[
                           contours[0]], contourIdx=-1, color=(0, 0, 255), thickness=2)

""" 
cv2.imshow('img', img_cnt)
cv2.waitKey(0)
"""

# Pole konturu
area = cv2.contourArea(contour=contours[4], oriented=True)

maxArea = 0
for e in range(len(contours)):
    contourArea = cv2.contourArea(contour=contours[e], oriented=True)
    if contourArea > maxArea:
        maxArea = contourArea
print(maxArea)

perimiter = cv2.arcLength(curve=contours[11], closed=True)
print(perimiter)
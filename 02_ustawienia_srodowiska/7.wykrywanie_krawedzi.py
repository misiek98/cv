import cv2
import imutils

# Canny Edge Detection to popularny algorytm do wyszukiwania krawędzi

img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\guido.jpg')
img = imutils.resize(img, height=500)
# cv2.imshow('img', img)

canny = cv2.Canny(image=img, threshold1=255, threshold2=250)
# cv2.imshow('canny', canny)

# cv2.waitKey(0)


for thresh in (0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250):
    canny = cv2.Canny(image=img, threshold1=thresh, threshold2=thresh)
    cv2.imshow(f'Canny: {thresh}', canny)
    cv2.waitKey(2000)
    cv2.destroyWindow(f'Canny: {thresh}')

import cv2
import imutils

img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\view.jpg')
logo = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\python.png')
logo = imutils.resize(logo, height=150)

""" 
cv2.imshow('Widok', img)
cv2.imshow('Logo', logo)
cv2.waitKey(0)
"""

# wycięcie obszaru roi - region of interest
rows, cols, channels = logo.shape
roi = img[:rows, :cols]
""" 
cv2.imshow('roi', roi)
cv2.waitKey(0)
"""
gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
"""
cv2.imshow('Szare logo', gray)
cv2.waitKey(0)
"""

# funkcja threshold zwraca 2 elementy, 1 to obraz
mask = cv2.threshold(src=gray, thresh=220, maxval=255,
                     type=cv2.THRESH_BINARY)[1]
"""
cv2.imshow('Maska logo', mask)
cv2.waitKey(0)
"""

# funkcja bitwise_not odwraca kolory
mask_inv = cv2.bitwise_not(mask)
"""
cv2.imshow('Maska loga odwrócona', mask_inv)
cv2.waitKey(0)
"""

img_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)
img_fg = cv2.bitwise_and(src1=logo, src2=logo, mask=mask_inv)
"""
cv2.imshow('Image foreground', img_fg)
cv2.imshow('Image background', img_bg)
cv2.waitKey(0)
"""

dst = cv2.add(src1=img_bg, src2=img_fg)
img[:rows, :cols] = dst
cv2.imshow('Out', img)
cv2.waitKey(0)

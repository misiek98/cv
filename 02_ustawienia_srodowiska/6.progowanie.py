import cv2

img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\grey.png')

# thresh_binary = cv2.threshold(img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]

for thresh in [0, 50, 100, 150, 200]:
    thresh_binary = cv2.threshold(
        src=img, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.imshow(f'thresh_binary: {thresh}', thresh_binary)
    cv2.waitKey(1000)
    cv2.destroyWindow(f'thresh_binary: {thresh}')

cv2.waitKey(0)

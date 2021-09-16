import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\checkbox.png')
img = cv2.copyMakeBorder(src=img,
                         top=20,
                         bottom=20,
                         left=20,
                         right=20,
                         borderType=cv2.BORDER_CONSTANT,
                         value=(255, 255, 255))

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)

thresh = cv2.threshold(src=blurred, thresh=75,
                       maxval=200, type=cv2.THRESH_BINARY)[1]

contours = cv2.findContours(
    image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'Długość listy konturów wynosi: {len(contours)}')

img_cnt = cv2.drawContours(image=img.copy(), contours=[
                           contours[5]], contourIdx=-1, color=(0, 0, 255), thickness=2)

# Wyszukanie konturu z zaznaczonym checkboxem
checked_idx = None
total = 0

for idx in [1, 2]:
    # wygenerowanie maski
    mask = np.zeros(shape=gray.shape, dtype='uint8')
    cv2.drawContours(mask, [contours[idx]],
                     contourIdx=-1, color=255, thickness=-1)
    # cv2.imshow(f'mask {idx}', mask)

    mask_inv = cv2.bitwise_not(mask)
    # cv2.imshow(f'mask_inv {idx}', mask_inv)

    answer = cv2.add(gray, mask_inv)
    # cv2.imshow(f'answer {idx}', answer)

    answer_inv = cv2.bitwise_not(answer)
    # cv2.imshow(f'answer_inv {idx}', answer_inv)

    cnt = cv2.countNonZero(answer_inv)
    if cnt > total:
        checked_idx = idx

print(checked_idx)

img = cv2.drawContours(image=img, contours=[
                       contours[checked_idx]], contourIdx=-1, color=(0, 0, 255), thickness=2)
cv2.imshow('checked_contour', img)

cv2.waitKey(0)

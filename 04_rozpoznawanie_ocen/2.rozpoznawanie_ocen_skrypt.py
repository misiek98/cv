import cv2
import imutils
import numpy as np
from imutils import contours
import argparse


def prepare_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 70, 70)
    thresh = cv2.threshold(
        edges, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return thresh


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to image')
args = vars(ap.parse_args())

print(f'OpenCV version: {cv2.__version__}')

# Klucz odpowiedzi
ANSWER_KEY = {0: 1,
              1: 3,
              2: 0,
              3: 2,
              4: 1,
              5: 3,
              6: 4,
              7: 1,
              8: 3,
              9: 0}

# Wczytanie obrazu
image = cv2.imread(args['image'])

# przygotowanie obrazu
thresh = prepare_image(image)

# wyszukanie wszystkich konturów
cnts = cv2.findContours(image=thresh.copy(),
                        mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print(f'[INFO] Liczba wykrytych konturów: {len(cnts)}')

# wyszukanie konturów z odpowiedziami
question_contours = []

for cnt in cnts:
    (x, y, w, h) = cv2.boundingRect(cnt)
    aspect_ratio = w / float(h)

    if w > 50 and h > 50 and aspect_ratio > 0.9 and aspect_ratio < 1.1:
        question_contours.append(cnt)

print(f'[INFO] Liczba wykrytych odpowiedzi: {len(question_contours)}')

img = image.copy()

# przetwarzanie obrazu
correct = 0
question_contours = imutils.contours.sort_contours(
    question_contours, method='top-to-bottom')[0]

for question, idx in enumerate(range(0, len(question_contours), 5)):
    fields = question_contours[idx:idx+5]
    fields = imutils.contours.sort_contours(fields, method='left-to-right')[0]

    marked = None

    for cnt_idx, cnt in enumerate(fields):
        mask = np.zeros(thresh.shape, dtype='uint8')

        # wyrysowanie konturu na masce
        cv2.drawContours(mask, [cnt], -1, 255, -1)

        # przeprowadzamy operację bitwise_and na obrazie thresh
        mask = cv2.bitwise_and(thresh, thresh, mask=mask)

        # zliczamy ilość pixeli niezerowych
        total = cv2.countNonZero(mask)

        if marked is None or total > marked[0]:
            marked = (total, cnt_idx)

    color = (0, 0, 255)

    key = ANSWER_KEY[question]

    if key == marked[1]:
        color = (0, 255, 0)
        correct += 1

    cv2.drawContours(img, [fields[key]], -1, color, 2)

cv2.imshow('Image', img)


checked = cv2.copyMakeBorder(
    img, 50, 0, 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
score = (correct / 10)

color = (50, 168, 82) if score >= 0.6 else (71, 7, 219)
text = 'Passed' if score >= 0.6 else 'Failed'

cv2.putText(img=checked, text=f'{text}: {score * 100}%', org=(1, 30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.9, color=color, thickness=2)
cv2.imshow('Checked', checked)
cv2.waitKey(0)


# python C:\Users\Misiek\Desktop\cv\4.rozpoznawanie_ocen\2.rozpoznawanie_ocen_skrypt.py -i C:\Users\Misiek\Desktop\cv\Obrazy\answers_1.png
# python C:\Users\Misiek\Desktop\cv\4.rozpoznawanie_ocen\2.rozpoznawanie_ocen_skrypt.py -i C:\Users\Misiek\Desktop\cv\Obrazy\answers_2.png

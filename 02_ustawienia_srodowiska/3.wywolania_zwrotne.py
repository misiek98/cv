import cv2


def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'x={x}, y={y}')


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (0, 0, 255), -1)


img = cv2.imread(r'C:\Users\Misiek\Desktop\cv\Obrazy\tesla.jpg')

cv2.namedWindow('Tesla')
cv2.setMouseCallback('Tesla', draw_circle)

# W momencie naciśnięcia klawisza ESC okno się zamyka i pętla zostaje przerwana
while True:
    cv2.imshow('Tesla', img)
    if cv2.waitKey(1) == 27:
        break

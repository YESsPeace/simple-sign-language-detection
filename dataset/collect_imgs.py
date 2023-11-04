import os

import cv2

from functions import Camera, button_handler, draw_text

DATA_DIR = '../data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

dataset_size = 100

cam = Camera()
cam.camera_num = 8
cap, camera_num = cam.get_capture()

for j in range(14, 15):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()

        cv2.putText(
            img=frame,
            text='Ready? Press "R"!',
            org=(225, 25),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1,
            color=(203, 65, 84)[::-1],
            thickness=2,
            lineType=cv2.LINE_AA
        )

        frame = draw_text(frame, camera_num)

        cv2.imshow('frame', frame)

        pressed_key = cv2.waitKey(1)

        if pressed_key == ord('q'):
            break

        else:
            cap, camera_num = button_handler(pressed_key, cam, cap, camera_num)

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()

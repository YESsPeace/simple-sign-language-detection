import pickle
import time

import cv2
import mediapipe as mp

from functions import recognize_hand_sign, Camera, draw_hand_landmarks, button_handler, draw_text

# importing the ML model

cam = Camera()
cam.camera_num = 8
cap, camera_num = cam.get_capture()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(False)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

previous_time = 0
current_time = 0

while True:
    ret, frame = cap.read()

    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    cv2.putText(
        img=frame,
        text='Wanna quit? Press "ESC"!',
        org=(225, 25),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=(203, 65, 84)[::-1],
        thickness=2,
        lineType=cv2.LINE_AA
    )

    frame = draw_text(frame, camera_num)

    if results.multi_hand_landmarks:  # if we have any hands

        # getting data from hand_landmarks
        for hand_landmarks in results.multi_hand_landmarks:
            prediction, sign_name, similarity, x_, y_ = recognize_hand_sign(frame, hand_landmarks)

            print(f'Predicted sign: code: "{prediction}", name: "{sign_name}", similarity: "{similarity}"')

            frame = draw_hand_landmarks(frame, hand_landmarks, sign_name, similarity, x_, y_)

    # getting the framerate
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time

    cv2.putText(
        img=frame,
        text=str(int(fps)),
        org=(10, 30),
        fontFace=cv2.FONT_HERSHEY_PLAIN,
        fontScale=2,
        color=(68, 148, 74)[::-1],
        thickness=2,
    )

    # showing the image
    cv2.imshow('python', frame)

    pressed_key = cv2.waitKey(1)

    # exit on ESC
    if pressed_key == 27:
        break

    else:
        cap, camera_num = button_handler(pressed_key, cam, cap, camera_num)

cv2.destroyWindow("python")
cap.release()
cv2.waitKey(1)

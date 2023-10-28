import pickle
import time

import cv2
import mediapipe as mp

from functions import recognize_hand_sign, get_capture

# importing the ML model
model = pickle.load(open('model/model.pickle', 'rb'))

cap, camera_num = get_capture()

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

    cv2.putText(
        img=frame,
        text=f'Camera: {camera_num}',
        org=(10, 60),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.75,
        color=(203, 65, 84)[::-1],
        thickness=1,
        lineType=cv2.LINE_AA
    )

    cv2.putText(
        img=frame,
        text=f'to change "<" and ">"',
        org=(10, 80),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.7,
        color=(203, 65, 84)[::-1],
        thickness=1,
        lineType=cv2.LINE_AA
    )

    if results.multi_hand_landmarks:  # if we have any hands

        # getting data from hand_landmarks
        for hand_landmarks in results.multi_hand_landmarks:
            prediction, sign_name, probability, x_, y_ = recognize_hand_sign(frame, model, hand_landmarks)

            print(f'Predicted sign: code: "{prediction}", name: "{sign_name}", probability: "{probability}"')

            # making the interface
            x1 = int(min(x_) * W) - 15
            y1 = int(min(y_) * H) - 15

            x2 = int(max(x_) * W) + 15
            y2 = int(max(y_) * H) + 15

            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing.DrawingSpec(color=(203, 65, 84)[::-1], thickness=2,
                                       circle_radius=2),  # hand points
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2,
                                       circle_radius=2),  # hand lines
            )

            cv2.rectangle(
                frame,
                (x1, y1), (x2, y2),
                color=(203, 65, 84)[::-1],
                thickness=3,
            )

            cv2.putText(
                img=frame,
                text=f"{sign_name} - {probability}",
                org=(x1, y1 - 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(203, 65, 84)[::-1],
                thickness=1,
                lineType=cv2.LINE_AA
            )

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

    if pressed_key in [44, 60]:
        cap, camera_num = get_capture(camera_num, -1)

    elif pressed_key in [46, 62]:
        cap, camera_num = get_capture(camera_num, 1)

    elif pressed_key == 27:  # exit on ESC
        break

cv2.destroyWindow("python")
cap.release()
cv2.waitKey(1)

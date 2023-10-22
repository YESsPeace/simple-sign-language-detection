import pickle
import time

import cv2
import mediapipe as mp

from functions import recognize_hand_sign

# importing the ML model
model = pickle.load(open('model/model.pickle', 'rb'))

# connecting the camera
cap = cv2.VideoCapture(1)  # for no reason my webcam is by number 6
cap.set(3, 640)  # Width
cap.set(4, 480)  # Length
cap.set(10, 100)  # Brightness

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
        org=(100, 50),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.3,
        color=(203, 65, 84)[::-1],
        thickness=3,
        lineType=cv2.LINE_AA
    )

    if results.multi_hand_landmarks:  # if we have any hands

        # getting data from hand_landmarks
        for hand_landmarks in results.multi_hand_landmarks:
            prediction, sign_name, x_, y_ = recognize_hand_sign(frame, model, hand_landmarks)

            print(f'Predicted sign: code: "{prediction}", name: "{sign_name}"')

            # making the interface
            x1 = int(min(x_) * W) - 15
            y1 = int(min(y_) * H) - 15

            x2 = int(max(x_) * W) + 15
            y2 = int(max(y_) * H) + 15

            cv2.rectangle(
                frame,
                (x1, y1), (x2, y2),
                color=(48, 186, 143)[::-1],
                thickness=3,
            )

            cv2.putText(
                img=frame,
                text=sign_name,
                org=(x1, y1 - 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(48, 186, 143)[::-1],
                thickness=2,
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
    if cv2.waitKey(20) == 27:  # exit on ESC
        break

cv2.destroyWindow("python")
cap.release()
cv2.waitKey(1)

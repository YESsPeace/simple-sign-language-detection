import pickle
import time

import cv2
import mediapipe as mp

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# importing the ML model
model = pickle.load(open('model.pickle', 'rb'))

# connecting the camera
cap = cv2.VideoCapture(6)  # for no reason my webcam is by number 6
cap.set(3, 640)  # Width
cap.set(4, 480)  # Length
cap.set(10, 100)  # Brightness

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(False)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

pTime = 0
cTime = 0

signs_dict = {
    0: 'Like',
    1: 'Like front',
    2: 'Like inv',
    3: 'Dislike',
    4: 'Dislike front',
    5: 'Dislike inv',
    6: 'Ok',
    7: 'Ok inv',
    8: 'Peace',
    9: 'Peace inv',
    10: 'Rock',
    11: 'Rock inv',
    12: 'YessPeace',
    13: 'YessPeace inv',
}

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
        inputs = []  # data which model will predict
        x_ = []
        y_ = []

        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                inputs.append(x - min(x_))
                inputs.append(y - min(y_))

            x1 = int(min(x_) * W) - 10
            y1 = int(min(y_) * H) - 10

            x2 = int(max(x_) * W) - 10
            y2 = int(max(y_) * H) - 10

        inputs = np.array(inputs).reshape(1, -1)

        if len(inputs[0]) > 41:
            inputs = [inputs[0][:42]]

        prediction = int(model.predict(inputs)[0])

        print(signs_dict[prediction])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)  # framerate

    cv2.imshow('python', frame)
    if cv2.waitKey(20) == 27:  # exit on ESC
        break

cv2.destroyWindow("python")
cap.release()
cv2.waitKey(1)

import pickle
import time

import cv2
import mediapipe as mp
import numpy as np

# importing the ML model
model = pickle.load(open('model/model.pickle', 'rb'))

# connecting the camera
cap = cv2.VideoCapture(6)  # for no reason my webcam is by number 6
cap.set(3, 640)  # Width
cap.set(4, 480)  # Length
cap.set(10, 100)  # Brightness

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(False)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

previous_time = 0
current_time = 0

signs_dict = {
    '0': 'Like',
    '1': 'Like front',
    '2': 'Dislike',
    '3': 'Dislike front',
    '4': 'Ok',
    '5': 'Peace',
    '6': 'Rock',
    '7': 'YessPeace sign',
    '8': 'Shaka',
    '9': 'Fuck you',
    '10': 'Spock',
    '11': 'West Coast',
    '12': 'East Coast',
    '13': 'Crips',
    '14': 'Bloods',
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

        # getting data from hand_landmarks
        for hand_landmarks in results.multi_hand_landmarks:
            inputs = []  # data which model will predict
            x_ = []
            y_ = []

            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            # getting all coordinates of hands landmarks
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            # getting relative coordinates of hands landmarks
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                inputs.append(x - min(x_))
                inputs.append(y - min(y_))

            # preparing data for the model
            inputs = np.array(inputs).reshape(1, -1)

            if len(inputs[0]) > 41:
                inputs = [inputs[0][:42]]

            # getting model prediction
            prediction = model.predict(inputs)[0]
            sign_name = signs_dict[prediction.split('_')[0]]

            print('Predicted sign:', 'code:', prediction, 'name:', sign_name)

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

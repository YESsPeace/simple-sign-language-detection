import cv2
import numpy as np
import mediapipe as mp
import time
import os

# Подключаем камеру
cap = cv2.VideoCapture(7)  # for no reason my webcam is by number 7
cap.set(3, 640)  # Width
cap.set(4, 480)  # Lenght
cap.set(10, 100)  # Brightness

mpHands = mp.solutions.hands
hands = mpHands.Hands(False)
npDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror flip

    cv2.putText(img, 'Wonna quite? Press "ESC" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                cv2.LINE_AA)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, lm)
                if id == 8 or id == 12:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

            npDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)  # framerate

    cv2.imshow('python', img)
    if cv2.waitKey(20) == 27:  # exit on ESC
        break

cv2.destroyWindow("python")
cap.release()
cv2.waitKey(1)
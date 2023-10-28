import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(False)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


def draw_hand_landmarks(img, hand_landmarks, sign_name, similarity, x1, y1, x2, y2):
    mp_drawing.draw_landmarks(
        img,  # image to draw
        hand_landmarks,  # model output
        mp_hands.HAND_CONNECTIONS,  # hand connections
        mp_drawing.DrawingSpec(color=(203, 65, 84)[::-1], thickness=2,
                               circle_radius=2),  # hand points
        mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2,
                               circle_radius=2),  # hand lines
    )

    cv2.rectangle(
        img,
        (x1, y1), (x2, y2),
        color=(203, 65, 84)[::-1],
        thickness=3,
    )

    cv2.putText(
        img=img,
        text=f"{sign_name} - {similarity}",
        org=(x1, y1 - 10),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=(203, 65, 84)[::-1],
        thickness=1,
        lineType=cv2.LINE_AA
    )

    return img

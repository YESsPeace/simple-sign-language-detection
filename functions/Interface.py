import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(False)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


def draw_hand_landmarks(img, hand_landmarks, sign_name, similarity, x_, y_):
    H, W, _ = img.shape

    x = W * H  # image resolution
    x_standard = 640 * 480

    thickness_dict = {
        'hand_landmarks_thickness': max(int(np.round((x * 2) / x_standard, 0)), 2),
        'rectangle_thickness': max(int(np.round((x * 3) / x_standard, 0)), 3),
        'font_scale': max(int(np.round((x * 1) / x_standard, 0)), 1),
        'text_thickness': max(int(np.round((x * 2) / x_standard, 0)), 2),
        'text_padding': max(int(np.round((x * 10) / x_standard, 0)), 10),
        'rectangle_padding': max(int(np.round((x * 15) / x_standard, 0)), 15),
    }

    mp_drawing.draw_landmarks(
        img,  # image to draw
        hand_landmarks,  # model output
        mp_hands.HAND_CONNECTIONS,  # hand connections
        mp_drawing.DrawingSpec(color=(203, 65, 84)[::-1], thickness=thickness_dict['hand_landmarks_thickness'],
                               circle_radius=thickness_dict['hand_landmarks_thickness']),  # hand points
        mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=thickness_dict['hand_landmarks_thickness'],
                               circle_radius=thickness_dict['hand_landmarks_thickness']),  # hand lines
    )

    x1 = int(min(x_) * W) - thickness_dict['rectangle_padding']
    y1 = int(min(y_) * H) - thickness_dict['rectangle_padding']

    x2 = int(max(x_) * W) + thickness_dict['rectangle_padding']
    y2 = int(max(y_) * H) + thickness_dict['rectangle_padding']

    cv2.rectangle(
        img,
        (x1, y1), (x2, y2),
        color=(203, 65, 84)[::-1],
        thickness=thickness_dict['rectangle_thickness'],
    )

    cv2.putText(
        img=img,
        text=f"{sign_name} {int(similarity * 100)}%",
        org=(x1, y1 - thickness_dict['text_padding']),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=thickness_dict['font_scale'],
        color=(203, 65, 84)[::-1],
        thickness=thickness_dict['text_thickness'],
        lineType=cv2.LINE_AA
    )

    return img

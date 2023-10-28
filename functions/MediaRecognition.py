import mediapipe as mp
import cv2

from functions import recognize_hand_sign, draw_hand_landmarks

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


def recognize_sign_from_img(img, model):
    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            prediction, sign_name, similarity, x_, y_ = recognize_hand_sign(img, model, hand_landmarks)
            img = draw_hand_landmarks(img, hand_landmarks, sign_name, similarity, x_, y_)

    # returning the image
    return img

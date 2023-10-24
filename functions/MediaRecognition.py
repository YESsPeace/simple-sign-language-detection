import mediapipe as mp
import cv2

from functions import recognize_hand_sign

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


def recognize_sign_from_img(img, model):
    pass

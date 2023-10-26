import mediapipe as mp
import cv2

from functions import recognize_hand_sign

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
            prediction, sign_name, probability, x_, y_ = recognize_hand_sign(img, model, hand_landmarks)
            # making the interface
            x1 = int(min(x_) * W) - 15
            y1 = int(min(y_) * H) - 15

            x2 = int(max(x_) * W) + 15
            y2 = int(max(y_) * H) + 15

            cv2.rectangle(
                img,
                (x1, y1), (x2, y2),
                color=(203, 65, 84)[::-1],
                thickness=3,
            )

            cv2.putText(
                img=img,
                text=f"{sign_name} - {probability}",
                org=(x1, y1 - 10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1,
                color=(203, 65, 84)[::-1],
                thickness=1,
                lineType=cv2.LINE_AA
            )

    # returning the image
    return img

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
            x1 = int(min(x_) * W) - ((H + W) // 74)
            y1 = int(min(y_) * H) - ((H + W) // 74)

            x2 = int(max(x_) * W) + ((H + W) // 74)
            y2 = int(max(y_) * H) + ((H + W) // 74)

            mp_drawing.draw_landmarks(
                img,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing.DrawingSpec(color=(203, 65, 84)[::-1], thickness=((H + W) // 560), circle_radius=((H + W) // 560)),  # hand points
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=((H + W) // 560), circle_radius=((H + W) // 560)),  # hand lines
            )

            cv2.rectangle(
                img,
                (x1, y1), (x2, y2),
                color=(203, 65, 84)[::-1],
                thickness=((H + W) // 373),
            )

            cv2.putText(
                img=img,
                text=f"{sign_name} - {probability}",
                org=(x1, y1 - ((H + W) // 112)),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=((H + W) // 1120),
                color=(203, 65, 84)[::-1],
                thickness=((H + W) // 1120),
                lineType=cv2.LINE_AA
            )

    # returning the image
    return img

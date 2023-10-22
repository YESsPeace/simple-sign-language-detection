import os
import pickle

import mediapipe as mp
import cv2

from functions import get_data_from_hand_landmarks

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

DATA_DIR = '../data'

data = []  # dataset's data
labels = []  # dataset's labels

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                img, data_aux = get_data_from_hand_landmarks(img, hand_landmarks)

                data.append(data_aux)
                labels.append(dir_)

# saving our dataset into .pickle file
with open('dataset_dictionary.pickle', 'wb') as file:
    pickle.dump({
        'data': data,
        'labels': labels,
    }, file)

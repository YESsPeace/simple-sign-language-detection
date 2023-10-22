import cv2


def get_capture(camera_num: int = 0):
    cap = cv2.VideoCapture(camera_num)
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Length
    cap.set(10, 100)  # Brightness

    return cap

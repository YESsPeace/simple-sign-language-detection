import cv2


def get_capture(camera_num: int = 0, change: int = None):
    if change:
        camera_num += change

    cap = cv2.VideoCapture(camera_num)
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Length
    cap.set(10, 100)  # Brightness

    print('Camera changed:', camera_num)

    return cap, camera_num

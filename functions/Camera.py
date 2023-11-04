import cv2


class Camera:
    camera_num = 0
    orientation = 'horizontal'

    def get_capture(self):
        cap = cv2.VideoCapture(self.camera_num)

        if self.orientation == 'vertical':
            cap.set(3, 480)  # Width
            cap.set(4, 640)  # Length

        else:
            cap.set(3, 640)  # Width
            cap.set(4, 480)  # Length

        cap.set(10, 100)  # Brightness

        return cap, self.camera_num

    def change_to_the_next_one(self):
        self.camera_num += 1

        return self.get_capture()

    def change_to_the_previous_one(self):
        self.camera_num -= 1

        return self.get_capture()

    def change_orientation(self):
        if self.orientation == 'vertical':
            self.orientation = 'horizontal'

        else:
            self.orientation = 'vertical'

        return self.get_capture()


def button_handler(ascii_code, cam, cap, camera_num):
    # change camera to one previous on "<"
    if ascii_code in [44, 60]:
        cap, camera_num = cam.change_to_the_previous_one()
        print('Camera changed:', camera_num)

    # change camera to one next on ">"
    elif ascii_code in [46, 62]:
        cap, camera_num = cam.change_to_the_next_one()
        print('Camera changed:', camera_num)

    # change orientation on "/"
    elif ascii_code in [47, 63]:
        cap.release()
        cap, camera_num = cam.change_orientation()

    return cap, camera_num

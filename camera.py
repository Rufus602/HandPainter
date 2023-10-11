import cv2
import time

Resolutions = [(360, 240), (720, 576), (960, 576), (1280, 720), (1920, 1080), (2592, 1520), (2592, 1920)]

class Camera_info():
    def __init__(self, cameraNo):
        self.cameraNo= cameraNo
        self.width, self.height = self.resolution_max()
        self.resolutions = self.find_resolutions()
    def find_resolutions(self):
        index = 0
        for x, y in Resolutions:
            if x < self.width and y < self.height:
                index+=1
                continue
            break
        resolutions = Resolutions[:index]
        resolutions.append((640, 480))
        return resolutions
    def resolution_max(self):
        cam = cv2.VideoCapture(self.cameraNo)
        w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return (int(w), int(h))



def all_cameras():
    return []





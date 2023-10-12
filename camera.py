import cv2
import time

class Camera_info():
    def __init__(self, cameraNo):
        self.cameraNo= cameraNo
        self.width, self.height = self.resolution_max()

    def resolution_max(self):
        cam = cv2.VideoCapture(self.cameraNo)
        w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return (int(w), int(h))



def all_cameras():
    something= [1, 2, 4]
    result = []
    for i in something:
        camera = Camera_info(i)
        result.append(['id', 'name', 'resolution'])
    return []





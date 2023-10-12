import cv2
import mediapipe as mp
import time
import os
import handTrackingModule as htm

class Paint():
    def __init__(self, cap, path, hands, draw, erase, place, cam_height, cam_width, color, size, detectCo, trackCo, mode = False):
        self.cap = cap
        self.path = path
        self.hands= hands
        self.draw = draw
        self.erase = erase
        self.place = place
        self.cam_height = cam_height
        self.cam_width = cam_width
        self.color = color
        self.size = size
        if hands == 0:
            hand_number = 2 # hands==0 means that we are using both hands
            self.detector = htm.handDetector(mode, hand_number, detectCo,trackCo)
        else:
            hand_number = 1  # hands==0 means that we are using both hands
            self.detector = htm.handDetector(mode, hand_number, detectCo, trackCo)
    def fingers(self):
        lms = self.detector.findPostions()

    def img(self):
        self.image = cv2.imread(self.path)

cap = cv2.VideoCapture(0)
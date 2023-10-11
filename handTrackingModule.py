import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode = False, handNo= 2, detectCo= 0.5, trackCo = 0.5):
        self.mode= mode
        self.handNo = handNo
        self.detectCo = detectCo
        self.trackCo = trackCo
        self.mpHand = mp.solutions.hands
        self.Hands = self.mpHand.Hands()
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self, img, draw = False):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.Hands.process(imgRGB)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHand.HAND_CONNECTIONS)
        return img
    def findPostions(self, img, handNo= 0, draw= True):
        lmsList = []
        h, w, _= img.shape
        if self.result.multi_hand_landmarks:
            hand = self.result.multi_hand_landmarks[handNo]
            for id, lms in enumerate(hand.landmark):
                cx, cy = int(lms.x * w), int(lms.y * h)

                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                lmsList.append([id, cx, cy])
        return lmsList

def main() :
    ctime = 0
    ptime =0
    cap  = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        ctime = time.time()
        fps= 1/(ctime-ptime)
        ptime = ctime
        cv2.putText(img, str(int(fps)),(20, 30), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
        img = detector.findHands(img)
        lms= detector.findPostions(img)
        if len(lms )!= 0:
            print(lms[4])
        cv2.imshow("Example", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
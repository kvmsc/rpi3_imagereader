from picamera import PiCamera
from time import sleep
import cv2

class Photo:
    def __init__(self,PATH):
        self.path = PATH
        self.array = None

    def capture(self):
        camera = PiCamera()
        camera.color_effects = (128,128) #capturing Black and White
        sleep(5)
        camera.capture(self.path)

    def preprocess(self):
        img = cv2.imread(PATH, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.array = gray


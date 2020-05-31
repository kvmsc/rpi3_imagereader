from pireader import Photo, Text, Speak
import RPi.GPIO as GPIO

state = 0
PATH = "/home/pi/Desktop/image.jpg"
image = Photo.Photo(PATH)
text = Text.Text()
speaker = Speak.Speak()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #use physical pin numbers
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set initial value to be low

def capture_and_speak():
    image.capture()
    image.preprocess()
    text.readImage(image)
    speaker.talk(text.data)
    state+=1

def callback_func(channel):
    if state==0
        capture_and_speak()
    if state==1:
        if not speaker.stopTalk():
            capture_and_speak()
            state=1
        else
            state=0

def main():
    speaker.talk("The device is starting!")
    speaker.talk("Ready! Press button to capture image.")
    
    while(True):
        GPIO.add_event_detect(10,GPIO.RISING,callback=callback_func)


if __name__== "__main__":
    main()

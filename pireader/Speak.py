import subprocess

class Speak:
    def __init__(self):
        self.speed = 200
        self.process = None
    
    def talk(self,text):
        self.process = subprocess.Popen(["espeak",'"{}"'.format(text)],
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE)
    
    def stopTalk(self):
        if self.process.poll()==0:
            return False
        self.process.terminate()
        self.talk("Ready! Press the button to start capture.")
        return True

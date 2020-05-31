import pytesseract

class Text:
    def __init__(self):
        self.langconf = "eng"
        self.oemconf = 3
        self.psmconf = 6
        self.data = None

    def readImage(self,photo):
        convtext = pytesseract.image_to_string(photo.array,
                                        config='-l {} --oem {} --psm {}'.format(
                                            self.langconf,self.oemconf,self.psmconf))
        self.data = convtext
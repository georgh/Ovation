import sys

class TextIO:
    history=[]
    def __init__(self, file = sys.stdin):
        self.file = file
        print ("Using Text")
        
    def wait(self):
        line=self.readline()
        print("Wait", line)
        return line and "en"

    def sentence(self):
        line=self.readline()
        print("Sentence:", line)
        return line

    def say(self,response):
        self.history.append(response)
        print(response)

    def eof(self):
        return self.file.eof()

    def readline(self):
        return self.file.readline().split("\n")[0]

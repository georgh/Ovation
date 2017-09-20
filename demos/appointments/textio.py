import sys

class TextIO:
    def __init__(self):
        print ("Using Text")
        
    def wait(self):
        line=self.readline()
        print("Wait", line)
        return "en"

    def sentence(self):
        line=self.readline()
        print("Sentence:", line)
        return line

    def say(self,response):
        print(response)

    def eof(self):
        return sys.stdin.eof()

    def readline(self):
        return sys.stdin.readline().split("\n")[0]

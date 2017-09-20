import sys

class TextIO:
    history=[]
    def __init__(self, file = sys.stdin):
        print ("Using Text-Mode! Start with a greeting in english or german:")
        self.file = file
        
    def wait(self):
        print("YOU: ", end='', flush=True)
        line=self.readline()
        print("Only english available at the moment...")
        return line and "en"

    def sentence(self):
        print("YOU: ", end='', flush=True)
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

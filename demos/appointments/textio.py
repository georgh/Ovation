import sys

class TextIO:
    def __init__(self):
        print ("Using Text-Mode! Start with a greeting in english or german:")
        
    def wait(self):
        print("YOU: ", end='', flush=True)
        line=self.readline()
        print("Only english available at the moment...")
        return "en"

    def sentence(self):
        print("YOU: ", end='', flush=True)
        line=self.readline()
        print("Sentence:", line)
        return line

    def say(self,response):
        print(response)

    def eof(self):
        return sys.stdin.eof()

    def readline(self):
        return sys.stdin.readline().split("\n")[0]

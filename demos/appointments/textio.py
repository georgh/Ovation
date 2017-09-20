import sys

class TextIO:
    history=[]
    def __init__(self, file = sys.stdin):
        self.file = file
        
    def initConversation(self):
        print ("\nUsing Text-Mode! Start with a greeting in english or german:")
        print("YOU: ", end='', flush=True)
        line = self.readline()
        print("", end="\r", flush=True)
        print("YOU: " + line, flush=True)
        print("Only english available at the moment...")
        return line and "en"

    def waitForSentence(self):
        print("YOU: ", end='', flush=True)
        line = self.readline()
        print("", end="\r", flush=True)
        print("YOU: " + line, flush=True)
        return line

    def say(self,response):
        self.history.append(response)
        print("\x1b[1;37;41m" + "BOT:" + "\033[0m " + response )

    def eof(self):
        return self.file.eof()

    def readline(self):
        return self.file.readline().split("\n")[0]

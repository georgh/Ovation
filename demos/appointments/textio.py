import os
import sys


class TextIO:
    history=[]
    def __init__(self, file = sys.stdin):
        self.file = file
        
    def initConversation(self):
        # print ("\nUsing Text-Mode! Start with a greeting in english or german:")
        # line = self.waitForSentence()
        # print("Only english available at the moment...")
        return "en"

    def waitForSentence(self):
        if not self.file == sys.stdin or not os.isatty(0): #read from file or use pipe
            line = self.readline()
            if line:
                print("\x1b[1;30;42m" + "USR:" + "\033[0m " + line, flush=True)
        else:
            print("\x1b[1;30;42m" + "USR:" + "\033[0m ", end='', flush=True)
            line = self.readline()
        return line

    def say(self,response):
        self.history.append(response)
        print("\x1b[1;30;44m" + "BOT:" + "\033[0m " + response )

    def eof(self):
        return self.file.eof()

    def readline(self):
        return self.file.readline().split("\n")[0]

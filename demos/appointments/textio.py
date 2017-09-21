import os
import sys


class TextIO:
    history=[]
    def __init__(self, file = sys.stdin):
        self.file = file
        self.eof = False

    def initConversation(self):
        print("Using Text")
        

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

    def readline(self):
        line = self.file.readline()
        if not line:
            self.eof = True
        return line.split("\n")[0]

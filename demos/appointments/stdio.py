import sys
import os

class StdIO:
    history=[]
    def __init__(self):
        print("Using StdIO")
        self.file = sys.stdin
        self.eof = False

    def check(self):
        return not self.eof
        

    def waitForSentence(self):
        if not os.isatty(0): # use pipe
            line = self.readline()
            print("\x1b[1;37;42m" + "YOU:" + "\033[0m " +line, flush=True)
        else:
            print("\x1b[1;37;42m" + "YOU:" + "\033[0m ", end='', flush=True)
            line = self.readline()
        return line

    def say(self,response):
        self.history.append(response)
        print("\x1b[1;30;44m" + "BOT:" + "\033[0m " + response )

    def readline(self):
        line = self.file.readline()
        if not line:
            self.eof = True
            return line
        else:
            return line.split("\n")[0]



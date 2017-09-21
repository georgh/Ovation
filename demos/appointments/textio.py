import sys


class TextIO:
    history=[]
    def __init__(self, file = sys.stdin):
        print("Using Text")
        self.file = file
        self.eof = False

    def check(self):
        self.readline_ahead()
        return not self.eof
        

    def waitForSentence(self):
        line = self.readline()
        if line:
            print("\x1b[1;30;42m" + "USR:" + "\033[0m " + line, flush=True)
        return line

    def say(self,response):
        self.history.append(response)
        print("\x1b[1;30;44m" + "BOT:" + "\033[0m " + response )

    def readline_ahead(self):
        line = self.file.readline()
        if not line:
            self.eof = True
        self.curr_line = line.split("\n")[0]

    
    def readline(self):
        result = self.curr_line
        self.readline_ahead()
        return result


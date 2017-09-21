from logic.core import Intent, UserInput, ResultObject, SessionState
import audio

class Session:
    def __init__(self, io):
        self.lastResponse = None
        self.io = io

    def say(self,response):
        self.lastResponse = response
        self.io.say(response)

    def handleMetaCommand(self, userInput):
        if userInput.intent == Intent.REPEAT and self.lastResponse:
            return ResultObject("Sure: " + self.lastResponse)
        elif userInput.intent == Intent.WAIT:
            self.io.say("I'm waiting. Please say {} again, if you want to continue".format(audio.keyword))
            self.io.check()
            return ResultObject("I'm ready. I said: " + self.lastResponse, SessionState.CONTINUE)
        return None

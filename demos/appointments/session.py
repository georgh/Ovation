from logic.core import Intent, UserInput, ResultObject, SessionState


class Session:
    def __init__(self, io):
        self.lastResponse = ""
        self.io = io

    def repeatedResponse(self, response):
        return "Sure: " + self.lastResponse 

    def say(self,response):
        if response != self.repeatedResponse(self.lastResponse):
            self.lastResponse = response
        self.io.say(response)

    def handleMetaCommand(self, userInput):
        userInput=userInput[0]
        if userInput.intent == Intent.REPEAT and self.lastResponse:
            return ResultObject(self.repeatedResponse(self.lastResponse))
        elif userInput.intent == Intent.WAIT:
            self.io.say("I'm waiting. Please say {} again, if you want to continue".format("Hello"))
            self.io.check()
            return ResultObject("I'm ready. I said: " + self.lastResponse, SessionState.CONTINUE)
        return None

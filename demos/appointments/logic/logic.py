from enum import Enum

class Intent:
    AFFIRM="Accept"
    REJECT="Reject"
    GOODBYE="Exit"
    BLABLA="Blabla"

class SessionState(Enum):
    DONE = 0
    CONTINUE = 1


class UserInput:
    def __init__(self, text, intent, entities):
        self.text = text
        self.intent = intent
        self.entities = entities



class ResultObject:
    def __init__(self, text, session_state):
        self.text = text
        self.session_state = session_state


# The input is a json object returned by RASA
def response(user_input):
    intent = user_input.intent 
    print("Interprete ", intent)
    
    if intent  == Intent.AFFIRM:
        return ResultObject("You can come, your appointment is booked", SessionState.DONE)

    if intent == Intent.REJECT:
        return ResultObject("BotQuestion", SessionState.CONTINUE)

    if intent == Intent.GOODBYE:
        return ResultObject("Goodbye and see you soon!", SessionState.DONE)

    return ResultObject("Sorry, I did not quite understand what you said...", SessionState.CONTINUE)


from enum import Enum

class SessionState(Enum):
    DONE = 0
    CONTINUE = 1


class ResultObject:
    def __init__(self, text, session_state):
        self.text = text
        self.session_state = session_state


# The input is a json object returned by RASA
def response(json):
    print("Interprete ", json)

    if json is None:
        pass
        # TODO : clear state and prepare for new user

    intent_ranking=json['intent_ranking']

    if len(intent_ranking) == 0:
        return ResultObject("Sorry, I did not quite understand what you said...", SessionState.CONTINUE)

    name = intent_ranking[0]['name']
    if name  == "affirm":
        return ResultObject("You can come, your appointment is booked", SessionState.DONE)

    if name == "reject":
        return ResultObject("BotQuestion", SessionState.CONTINUE)

    if name == "goodbye":
        return ResultObject("Goodbye and see you soon!", SessionState.DONE)

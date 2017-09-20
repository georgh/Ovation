from enum import Enum

import logic.database as db
import logic.questionAnswer as qa


class SessionState(Enum):
    DONE = 0
    CONTINUE = 1


class ResultObject:
    def __init__(self, text, session_state):
        self.text = text
        self.session_state = session_state


        # TODO integrate a reasonable parsing of rasa

# The input is a json object returned by RASA
def response(json):
    print("Interprete ", json)

    # Session terminated and a we prepare a new fresh state for a new user
    if json is None:
        qa.clear()
        db.clear()
        db.loadFromFile()


    intent_ranking = json['intent_ranking']

    # RASA failed to understand the message
    if len(intent_ranking) == 0:
        return ResultObject("Sorry, I did not quite understand what you said...", SessionState.CONTINUE)

    name = intent_ranking[0]['name']

    # User is greeting the bot
    if name == "greet":
        return ResultObject(qa.nextQuestion(), SessionState.CONTINUE)

    # User is accepting the proposed appointment
    if name  == "affirm":
        # TODO remove from the list of calendar the now boooked appointment
        return ResultObject("You can come, your appointment is booked", SessionState.DONE)

    # User directly rejected the proposed appointment
    if name == "reject":
        return ResultObject("BotQuestion", SessionState.CONTINUE)

    # Just because we are nice, we say goodbye to user after an agreement is reached
    if name == "goodbye":
        return ResultObject("Goodbye and see you soon!", SessionState.DONE)

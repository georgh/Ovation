from enum import Enum
import logic.database as db
import logic.questionAnswer as qa

class Intent:
    AFFIRM="Accept"
    REJECT="Reject"
    GOODBYE="Exit"
    BLABLA="Blabla"
    GREET="Greet"



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


# TODO integrate a reasonable parsing of rasa

# The input is a json object returned by RASA
def response(user_input):
    intent = user_input.intent 
    print("Interprete ", intent)

    # new Session starts and a we prepare a new fresh state for a new user
    if intent  == Intent.GREET:
        qa.clear()
        db.clear()
        db.loadFromFile()

        return ResultObject("You can come, your appointment is booked", SessionState.DONE)

    # User is greeting the bot
    if intent == Intent.GREET:
        return ResultObject(qa.nextQuestion(), SessionState.CONTINUE)

    # User is accepting the proposed appointment
    if intent  == Intent.AFFIRM:
        # TODO remove from the list of calendar the now boooked appointment
        return ResultObject("You can come, your appointment is booked", SessionState.DONE)

    # User directly rejected the proposed appointment
    if intent == Intent.REJECT:
        return ResultObject("BotQuestion", SessionState.CONTINUE)

    # Just because we are nice, we say goodbye to user after an agreement is reached
    if intent == Intent.GOODBYE:
        return ResultObject("Goodbye and see you soon!", SessionState.DONE)

    return ResultObject("Sorry, I did not quite understand what you said...", SessionState.CONTINUE)


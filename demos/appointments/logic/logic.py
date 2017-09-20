from enum import Enum
import logic.database as db
import logic.questionAnswer as qa

class Intent:
    AFFIRM="Accept"
    REJECT="Reject"
    GOODBYE="Exit"
    BLABLA="Blabla"
    GREET="Greet"
    MAKE_AN_APPOINTMENT="Appointment"



class SessionState(Enum):
    DONE = 0
    CONTINUE = 1


class UserInput:
    def __init__(self, text, intent, entities=[]):
        self.text = text
        self.intent = intent
        self.entities = entities

GREETING=UserInput("Hi", Intent.GREET)        



class ResultObject:
    def __init__(self, text, session_state = SessionState.CONTINUE):
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

    # User is greeting the bot
    if intent == Intent.GREET:
        return ResultObject("Hello, what can I do for you?")        

    if intent == Intent.MAKE_AN_APPOINTMENT:
        return ResultObject(qa.nextQuestion())

    # User is accepting the proposed appointment
    if intent  == Intent.AFFIRM:
        # TODO remove from the list of calendar the now boooked appointment
        date, time = "2017-09-19", "09:00:00" #qa.getLastProposedTimeslot()
        return ResultObject("So the agent will call you on {} at {}. Thank you and goodbye.".format(date, time), SessionState.DONE)

    # User directly rejected the proposed appointment
    if intent == Intent.REJECT:
        #remove the last proposed slot from the list
        db.removeFirst()
        return ResultObject(qa.nextQuestion(), SessionState.CONTINUE)

    # Just because we are nice, we say goodbye to user after an agreement is reached
    if intent == Intent.GOODBYE:
        return ResultObject("Goodbye and see you soon!", SessionState.DONE)

    return ResultObject("Sorry, I did not quite understand what you said...", SessionState.CONTINUE)


from enum import Enum

import logic.database as db
import logic.questionAnswer as qa
from logic import restriction, parser


class Intent:
    AFFIRM="accept"
    REJECT="reject"
    GOODBYE="exit"
    BLABLA="blabla"
    MAKE_AN_APPOINTMENT="appointment"
    POSITIVE="positive"
    NEGATIVE="negative"
    REPEAT="repeat"
    WAIT="wait"

class Entity:
    def __init__(self, value, entity):
        self.entity = entity
        self.value = value

    def __repr__(self):
        return "{}: '{}'".format(self.entity, self.value)

class SessionState(Enum):
    DONE = 0
    CONTINUE = 1
    WAIT = 2


class UserInput:
    def __init__(self, text=None, intent=None, entities=[]):
        self.text = text
        self.intent = intent
        self.entities = entities

class ResultObject:
    def __init__(self, text, session_state = SessionState.CONTINUE):
        self.text = text
        self.session_state = session_state


# The input is a json object returned by RASA
def response(user_input):

    # if len(user_input) == 1:
    user_input = user_input[0]
    # else:


    intent = user_input.intent
    print("Intent:", intent, user_input.entities)

    ###########################################################################
    # MAKE_AN_APPOINTMENT
    # User want to schedule an appointment
    if intent == Intent.MAKE_AN_APPOINTMENT:
        return ResultObject(qa.nextQuestion())

    ###########################################################################
    # POSITIVE OR NEGATIVE
    # User is proposing a positive restriction
    if intent == Intent.POSITIVE or intent == Intent.NEGATIVE:
        # Apply restriction
        day = []
        hour = []
        for entity in user_input.entities:
            # if not pravinee.filter(entity) and entity.entity == 'day':
            val, status = parser.convertStrToDatetime(entity.value)
            if entity.entity == 'day' or  entity.entity == 'date' and status:
                    day += [val.day]

            if entity.entity == 'timespan':
                hour += [parser.convertToRange(entity.value)]

        restriction.apply(day=day, hour=hour, negative=(intent == Intent.POSITIVE))

        # Return next question
        return ResultObject("Ok, let me see... " + qa.nextQuestion())

    ###########################################################################
    # AFFIRM
    # User is accepting the proposed appointment
    if intent  == Intent.AFFIRM:
        # TODO remove from the list of calendar the now boooked appointment
        if len(db.timeslots) != 0:
            sl = qa.getLastProposedTimeslot()
            if sl == None:
                return ResultObject("STUPID! I DID NOT GIVE YOU A DATE YET! ehhh ... Please repeat your input.", SessionState.CONTINUE)
            else:
                return ResultObject(
                    "So the agent will call you " + parser.convertDatetimeToStr(sl) + ". Thank you and goodbye.",
                    SessionState.DONE)
        else:
            return ResultObject(
                "Thank you for your call. However, with the current schedule we " +
                "cannot satisfy your requests. Have a nice day!",
                SessionState.DONE)

    ###########################################################################
    # REJECT
    # User directly rejected the proposed appointment
    if intent == Intent.REJECT:
        # remove the last proposed slot from the list
        db.remove(qa.getLastProposedTimeslot())
        return ResultObject(qa.nextQuestion(), SessionState.CONTINUE)

    ###########################################################################
    # GOODBYE
    # Just because we are nice, we say goodbye to user after an agreement is reached
    if intent == Intent.GOODBYE:
        return ResultObject("Goodbye and see you soon!", SessionState.DONE)

    ## NOTE: We should check if the last restricions removes
    #  all available timeslots, if so we should tell the user
    # (maybe not apply it?)
    # -> is this a requirement from the PO ?

    return ResultObject("Sorry, I did not quite understand what you said...", SessionState.CONTINUE)


import json

from enum import Enum


class SessionState(Enum):
    DONE = 0
    CONTINUE = 1


class ResultObject:
    def __init__(self, text, session_state):
        self.text = text
        self.session_state = session_state


def response(text):
    print("Interprete ", text)
    return ResultObject("You can come now", SessionState.DONE)


# The input string would be the Json (one or more we still have to define) returned
# by RASA

# TODO add input parameter
# TODO add switch-case logic for the cases intent=accept, reject, exit
def processUserInput():
    from pprint import pprint
    
    with open('data.json') as data_file:
        data = json.load(data_file)
    
    pprint(data)

processUserInput()

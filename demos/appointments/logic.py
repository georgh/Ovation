from enum import Enum

class SessionState(Enum):
    DONE = 0
    CONTINUE = 1 
    

class ResultObject:
    def __init__(self, text, session_state):
        self.text = text
        self.session_state = session_state

    
def response(text):
    print ("Interprete ", text)
    return ResultObject("You can come now", SessionState.DONE)
    

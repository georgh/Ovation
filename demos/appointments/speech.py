import audio

        
class Speech():

    def __init__(self):
        print ("Using Speech")
        audio.init_threshold()
        
    def wait(self):
        print("Listening for keyword '", audio.keyword, "'", sep="")
        audio.passive_listen()
        return "en"

    def sentence(self):
        alts=audio.active_listen()[0]
        if alts: 
            return alts[0]
        else:
            return None

    def eof(self):
        return False

    def say(self,response):
        audio.say(response)

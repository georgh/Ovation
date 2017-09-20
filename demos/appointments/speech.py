import audio

        
class Speech():

    def __init__(self):
        print ("Using Speech")
        audio.init_threshold()
        
    def initConversation(self):
        print("Listening for keyword '", audio.keyword, "'", sep="")
        line = audio.passive_listen()
        print("YOU:", line)
        return "en"

    def waitForSentence(self):
        alts=audio.active_listen()
        if alts:
            print("YOU:", alts)
            return alts[0]
        else:
            return None

    def eof(self):
        return False

    def say(self,response):
        print("BOT:", response)
        audio.say(response)

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
        return audio.active_listen()[0]

    def say(self,response):
        audio.say(response)

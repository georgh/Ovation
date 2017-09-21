from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

from extractDates import findDates
from logic.core import UserInput, Entity
from logic.entityFilter import entityIsValid
from simpleMatch import trivial_intent
from extractDates import findDates, findTime

# from nltk.corpus import stopwords
# from nltk.tokenize import wordpunct_tokenize


USESPLIT = False

print("Loading rasa config....")
model_directory = './models/default'
config = RasaNLUConfig("config/config_mitie.json")
metadata = Metadata.load(model_directory)
interpreter = Interpreter.load(metadata, config )

def countIntentions(sen):
      stop_words =  set(["but"]) #set(stopwords.words('english'))
      stop_words.update(['.', ',', '?', '!', ':', ';']) # remove it if you need punctuation 
      list_of_words = sen.split

      current = [sen]

      for w in stop_words:
            #print(str(current)+ " stopwords: "+ w)
            newset = []
            for s in current:
                  sp = s.split(w)
                  if len(sp) > 1:
                        newset += [x.strip() for x in sp]
                  else:
                        newset += [s.strip()]
            current = newset
      current = list(filter(None, current)) #filter empty
      # . , : ;               
      #stopwords: 
      print(current)
      return current


def understand(sentence):
      sentence = sentence.lower()
      intent, entities, isTrivial = trivial_intent(sentence)
      if isTrivial:
            return [UserInput(sentence, intent, [Entity(sentence, entity) for entity in entities])]

      #check if the user has more then one intention:
      if USESPLIT:
            splittedSentence = countIntentions(sentence)
      else:
            splittedSentence = [sentence]

      resultingInputs = []
      for sen in splittedSentence:
            result = interpreter.parse(sen)
            print(result)
            # for v in result['intent_ranking']:
            #       print("    " +  str(v))
            extraDates = [Entity(date, 'date') for date in findDates(sen)]
            extraTimes = [Entity(hour, 'hours') for hour in findTime(sen)]
            entities = [Entity(item['value'], item['entity']) for item in result["entities"]]
            entities = [entity for entity in entities if entityIsValid(entity)]
            if "intent" in result:
                  resultingInputs += [UserInput(sen, result["intent"]["name"],
                           extraDates + extraTimes + entities)]
      # else:
      #   resultingInputs += [UserInput(sen, Intent.BLABLA)]
      if len(resultingInputs) == 0:
            return [UserInput(sen, Intent.BLABLA)]
      else:
            return resultingInputs

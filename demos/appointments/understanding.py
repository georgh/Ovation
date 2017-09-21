from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

from extractDates import findDates
from logic.core import UserInput, Entity
from logic.entityFilter import entityIsValid
from simpleMatch import trivial_intent
from extractDates import findDates



model_directory = './models/default'
config = RasaNLUConfig("config/config_mitie.json")
metadata = Metadata.load(model_directory)
interpreter = Interpreter.load(metadata, config )

def countIntentions(sen):
      return 1


def understand(sentence):
  sentence = sentence.lower()
  intent, isTrivial = trivial_intent(sentence)
  if isTrivial:
    return UserInput(sentence, intent)

  #check if the user has more then one intention:
  c = countIntentions(sentence)



  result = interpreter.parse(sentence)
  extraDates = [Entity(date, 'date') for date in findDates(sentence)]
  entities=[Entity(item['value'], item['entity']) for item in result["entities"]]
  entities=[entity for entity in entities if entityIsValid(entity)]
  if "intent" in result:
    return UserInput(sentence, result["intent"]["name"],
                     extraDates + entities)
  else:
    return UserInput(sentence, Intent.BLABLA)

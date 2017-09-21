from extractDates import findDates
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

from logic.core import UserInput, Entity
from simpleMatch import trivial_intent

model_directory = './models/default'
config = RasaNLUConfig("config/config_mitie.json")
metadata = Metadata.load(model_directory)
interpreter = Interpreter.load(metadata, config )

def understand(sentence):
    sentence = sentence.lower()
  intent = trivial_intent(sentence)
  if intent:
    return UserInput(sentence, intent)
  
  result = interpreter.parse(sentence)
    extraDates = [Entity(date, 'date') for date in findDates(sentence)]
    entities = [Entity(item['value'], item['entity']) for item in result["entities"]]
  if "intent" in result:
    return UserInput(sentence, result["intent"]["name"],
                     extraDates + entities)
  else:
    return UserInput(sentence, Intent.BLABLA)

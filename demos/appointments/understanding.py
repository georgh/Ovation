from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

from logic.core import UserInput

from simpleMatch import trivial_intent

model_directory = './models/default'
config = RasaNLUConfig("config/config_mitie+sklearn.json")
metadata = Metadata.load(model_directory)
interpreter = Interpreter.load(metadata, config )

def understand(sentence):
  intent = trivial_intent(sentence)
  if intent:
    return UserInput(sentence, intent, [])
  
  result = interpreter.parse(sentence)
  # print("### DEBUG:")
  # print("intent : " + str(result['intent']))
  # print("entities : " + str(result['entities']))
  # print('intent_ranking:')
  # for v in result['intent_ranking']:
  #     print("    " +  str(v))
  return UserInput(sentence, result["intent"]["name"], result["entities"])

from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

from logic.logic import UserInput

model_directory = './models/default'
config = RasaNLUConfig("config/config_mitie+sklearn.json")
metadata = Metadata.load(model_directory)
interpreter = Interpreter.load(metadata, config )

def understand(sentence):
  result = interpreter.parse(sentence)
  print("### DEBUG:")
  print("intent : " + str(result['intent']))
  print("entities : " + str(result['entities']))
  print('intent_ranking:')
  for v in result['intent_ranking']:
      print("    " +  str(v))
  return UserInput(sentence, result["intent"]["name"], result["entities"])

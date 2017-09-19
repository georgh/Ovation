from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Metadata, Interpreter

model_directory = './models/default'
config = RasaNLUConfig("config/config_mitie+sklearn.json")
metadata = Metadata.load(model_directory)
interpreter = Interpreter.load(metadata, config )

def understand(sentence):
  result = interpreter.parse(sentence)
  print(result)

import json

# The input string would be the Json (one or more we still have to define) returned
# by RASA

# TODO add input parameter
# TODO add switch-case logic for the cases intent=accept, reject, exit
def processUserInput():
    from pprint import pprint
    
    with open('data.json') as data_file:
        data = json.load(data_file)
    
    pprint(data)

processUserInput()

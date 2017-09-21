#import logic.core as l
import re

from logic.core import Intent

INTENT_MAP=[
    (Intent.GOODBYE, [
        "bye", "goodbye", "stop", "end", "farewell"
    ]),
    (Intent.AFFIRM, [
        "yes","yep","yeah","indeed","ok", "okay", "great", "accept", "correct", "perfect", "agreed", "agree"
    ]),
    (Intent.REJECT, [
        "no", "nope", 
    ]),
    (Intent.REPEAT,  [
        "repeat"
    ]),
    (Intent.WAIT, [
        "wait"
    ])
]

def trivial_intent(sentence):
    sentence = sentence.lower()
    sentence =re.sub('[\.! \?]', '', sentence)
    global INTENT_MAP
    for (intent, words) in INTENT_MAP:
        if sentence in words:
            return intent
    return None
        

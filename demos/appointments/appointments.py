#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logic import logic
from understanding import understand
from speech import Speech
from textio import TextIO
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument('l', type=str) #necessary string option
parser.add_argument('-t', '-text', '--text', action='store_true', default=False, help="Switch to text-only mode")
args = parser.parse_args() 

def listen_loop(io):
    while True:
        lang = io.wait()
        print("Listening for commands in", lang)
        sentence = io.sentence()
        if not sentence:
            break
        print("Commands received", sentence)
        answer = logic.response(understand(sentence))
        io.say(answer.text)

if args.text:
    backend=TextIO()
else:
    from speech import Speech
    backend=Speach()

listen_loop(backend)



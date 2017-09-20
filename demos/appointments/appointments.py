#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logic import logic
from understanding import understand
from textio import TextIO
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument('l', type=str) #necessary string option
parser.add_argument('-t', '-text', '--text', action='store_true', default=False, help="Switch to text-only mode")
args = parser.parse_args() 

def listen_loop(io):
    lang = io.wait()
    print("Listening for commands in", lang)
    greeting = logic.response(logic.GREETING)
    io.say(greeting.text)
    while True:
        sentence = io.sentence()
        if not sentence:
            break
        print("Commands received", sentence)
        answer = logic.response(understand(sentence))
        io.say(answer.text)
        if answer.session_state == logic.SessionState.DONE:
            break

if args.text:
    backend=TextIO()
else:
    from speech import Speech
    backend=Speech()

listen_loop(backend)



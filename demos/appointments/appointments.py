#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logic import logic
from understanding import understand
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument('l', type=str) #necessary string option
parser.add_argument('-t', '-text', '--text', action='store_true', default=False, help="Switch to text-only mode")
args = parser.parse_args() 

if not args.text:
    from speech import Speech

def listen_loop(io):
    while True:
        lang = io.wait()
        print("Listening for commands in", lang)
        sentence = io.sentence()

        print("Commands received", sentence)
        answer = logic.response(understand(sentence))
        io.say(answer.text)

if args.text:
    print("TEXT MODE NOT YET IMPLEMENTED")
else:
    listen_loop(Speech())



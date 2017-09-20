#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from speech import Speech
from logic import logic
from understanding import understand

def listen_loop(io):
    while True:
        lang = io.wait()
        print("Listening for commands in", lang)
        sentence = io.sentence()

        print("Commands received", sentence)
        answer = logic.response(understand(sentence))
        io.say(answer.text)

listen_loop(Speech())



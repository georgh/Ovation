#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import audio
import logic
from understanding import understand

def act(transcription):
    for alt in transcription:        
        print(alt)
        understand(alt)
        answer = logic.response(alt)
        audio.say(answer.text)
        return answer.session_state


def listen_loop():
    audio.init_threshold()

    while True:
        print("Listening for keyword 'appointment'")
        audio.passive_listen()
        print("Listening for commands")
        transcription = audio.active_listen()
        print("Commands received")
        if transcription:
            act(transcription)

listen_loop()



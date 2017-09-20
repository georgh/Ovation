#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logic import logic
from understanding import understand
from textio import TextIO

def listen_loop(io):
    while True:
        lang = io.initConversation()
        if not lang:
            break
        print("Current language: ", lang)
        greeting = logic.response(logic.GREETING)
        io.say(greeting.text)
        while True:
            sentence = io.waitForSentence()
            if not sentence:
                break
            answer = logic.response(understand(sentence))
            io.say(answer.text)
            if answer.session_state == logic.SessionState.DONE:
                break

def main():
    import argparse

    parser = argparse.ArgumentParser()
    #parser.add_argument('l', type=str) #necessary string option
    parser.add_argument('-t', '-text', '--text', action='store_true', default=False, help="Switch to text-only mode")
    parser.add_argument(
        '--dialog',
        dest='dialog',
        type=str,
        default="",
        help="validate dialog")
    args = parser.parse_args() 

    
    if args.text:
        import sys
        listen_loop(TextIO())
    elif args.dialog:
        with open(args.dialog) as infile:
            validate = open(args.dialog + ".output", "r").read().split("\n")
            backend = TextIO(infile)
            listen_loop(backend)
            if validate != backend.history:
                print("ERROR")
                print("GOT:\n", "\n".join(backend.history), sep="")
                print("Expected:\n", "\n".join(validate), sep="");
            else:
                print("SUCCESS");
    else:
        from speech import Speech
        listen_loop(Speech())


if __name__ == "__main__":
    main()





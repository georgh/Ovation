#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logic import core
from textio import TextIO
from understanding import understand


def listen_loop(io):
    while True:
        lang = io.initConversation()
        if not lang:
            break
        print("Current language: ", lang)
        greeting = core.response(core.GREETING)
        io.say(greeting.text)
        while True:
            sentence = io.waitForSentence()
            if not sentence:
                break
            answer = core.response(understand(sentence))
            io.say(answer.text)
            if answer.session_state == core.SessionState.DONE:
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
        listen_loop(TextIO())
    elif args.dialog:
        with open(args.dialog) as infile:
            validate = open(args.dialog + ".output", "r").read().split("\n")
            backend = TextIO(infile)
            listen_loop(backend)
            if validate != backend.history:
                print("\x1b[1;37;41m" + "#!# ERROR: #!#" + "\033[0m")
                # print("\x1b[1;37;41m" +"GOT:\n", "\n".join(backend.history) + "\033[0m", sep="")
                # print("\x1b[1;37;41m" + "Expected:\n", "\n".join(validate) + "\033[0m", sep="")
                print("GOT:\n", "\n".join(backend.history), sep="")
                print("Expected:\n", "\n".join(validate), sep="")
            else:
                print("\x1b[1;37;42m" + "#!# SUCCESS! #!#" + "\033[0m")
    else:
        from speech import Speech
        listen_loop(Speech())


if __name__ == "__main__":
    main()





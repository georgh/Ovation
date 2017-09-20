#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logic import core
from logic import database as db
from textio import TextIO


def listen_loop(io):
    io.say("Hello this is Ovation studio: how can we help you?")
    # i = 0
        while True:
            sentence = io.waitForSentence()
            if not sentence:
                break

            """
                # answer = core.response(core.UserInput(intent=core.Intent.AFFIRM))
                # answer = core.response(core.UserInput(intent=core.Intent.REJECT))
                # answer = core.response(core.UserInput(intent=core.Intent.GOODBYE))
                # answer = core.response(core.UserInput(intent=core.Intent.BLABLA))
                # answer = core.response(core.UserInput(intent=core.Intent.GREET))

            if i == 0:
                answer = core.response(core.UserInput(intent=core.Intent.MAKE_AN_APPOINTMENT))
            elif i == 1:
                answer = core.response(core.UserInput(intent=core.Intent.GOODBYE))
            elif i == 2:
                pass

            i += 1
            """
            answer = core.response(understand(sentence))

            io.say(answer.text)
            if answer.session_state == core.SessionState.DONE:
                break


def main():
    # Load the database
    db.loadFromFile()

    import argparse

    parser = argparse.ArgumentParser()
    # parser.add_argument('l', type=str) #necessary string option
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
            """
            if validate != backend.history:
                print("\x1b[1;30;41m" + "#!# ERROR: #!#" + "\033[0m")
                # print("\x1b[1;37;41m" +"GOT:\n", "\n".join(backend.history) + "\033[0m", sep="")
                # print("\x1b[1;37;41m" + "Expected:\n", "\n".join(validate) + "\033[0m", sep="")
                print("GOT:\n", "\n".join(backend.history), sep="")
                print("Expected:\n", "\n".join(validate), sep="")
            else:
                print("\x1b[1;37;42m" + "#!# SUCCESS! #!#" + "\033[0m")
            """
    else:
        from speech import Speech
        listen_loop(Speech())


if __name__ == "__main__":
    main()

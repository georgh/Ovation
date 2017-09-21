#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logic import core
from logic import database as db
from stdio import StdIO
from textio import TextIO
from understanding import understand


def listen_loop(io):
    while io.check():
        io.say("I am the ovation insurance chatbot: how can I help you?")
        session_state = core.SessionState.CONTINUE
        while session_state != core.SessionState.DONE:
            sentence = io.waitForSentence()
            if not sentence:
                return

            answer = core.response(understand(sentence))

            io.say(answer.text)
            session_state = answer.session_state


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
    parser.add_argument(
        '--record',
        action='store_true',
        help="overwrite text case output",
        default=False)
    args = parser.parse_args()

    if args.text:
        listen_loop(StdIO())
    elif args.dialog:
        with open(args.dialog) as infile:
            output_file=args.dialog + ".output"
            validate = not args.record and [line for line in open(output_file, "r").read().split("\n") if line] 
            backend = TextIO(infile)
            listen_loop(backend)
            if args.record:
                with open(output_file, "w+") as outfile:
                    outfile.write("\n".join(backend.history))
                    outfile.close()
            elif validate != backend.history:
                print("\x1b[1;30;41m" + "#!# ERROR: #!#" + "\033[0m")
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

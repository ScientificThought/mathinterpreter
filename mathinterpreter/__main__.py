import argparse
import readline
import sys

from mathinterpreter.calculate import calc


def main():

    nargs = len(sys.argv)
    repl = nargs == 1

    if nargs == 2:
        text = sys.argv[1]
        value = calc(text)
        print(value)

    while repl:

        try:
            text = input("calc > ")
        except KeyboardInterrupt:
            print("\n", KeyboardInterrupt.__doc__)
            exit()

        if text.isascii():
            text = text.lower()
            if text in ["q", "quit"]:
                break

        value = calc(text)
        print(value)


if __name__ == "__main__":
    main()

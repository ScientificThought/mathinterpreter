import argparse
import readline
import sys

from mathinterpreter.calculate import calc


def main():

    repl = len(sys.argv) == 1
    if not repl:
        cli(repl=repl)

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


def cli(repl):

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "operations",
        help="Calculate operations, where operations is an string containing"
        " a mathematical expression. "
        "To include spaces on this expressions use single or double dashes"
        ', \' or ", as in "1+1"',
        type=str,
    )
    args = parser.parse_args()

    value = calc(args.operations)
    print(value)
    exit()


if __name__ == "__main__":
    main()

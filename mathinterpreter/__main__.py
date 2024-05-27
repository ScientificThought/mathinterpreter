import argparse
import readline
import sys

from mathinterpreter.calculate import calc


def main():

    repl = len(sys.argv) == 1
    cli(repl=repl)

    while repl:

        try:
            text = input("calc > ")
        except KeyboardInterrupt:
            print("\n", KeyboardInterrupt.__doc__)
            exit()

        text = text.strip()
        if text.isascii():
            text = text.lower()
            if text in ["q", "quit"]:
                break

        if text:
            value = calc(text)
            if value:
                print(value)


def cli(repl):

    parser = argparse.ArgumentParser(
        description="A simple math interpreter with a command line interface and an interactive mode.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "expression",
        nargs="*",
        help="Evaluate expression, which must be in one of the following forms:\n"
        "  1+1/2^4\n"
        "  1 + 1 / 2^4\n"
        "  1 + 1 / '(2^(4/2))'\n"
        "Note that to properly include parenthesis on command line calls it is necessary to"
        " use single or double quotes, ' or \", enclosing the expression.\n"
        "Default: interactive mode.",
    )
    args = parser.parse_args()
    text = "".join(args.expression)

    if not repl:
        value = calc(text)
        print(value)


if __name__ == "__main__":
    main()

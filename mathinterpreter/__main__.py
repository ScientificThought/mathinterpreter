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
        except KeyboardInterrupt as e:
            print("\n", e.__doc__)
            exit()
        except EOFError:
            print("EOFError")
            exit()

        text = text.strip()
        if text.isascii():
            text = text.lower()
            if text in ["q", "quit"]:
                break
            print_value(text)
        else:
            print("Invalid input!")


def print_value(text):
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

    if not repl:
        args = parser.parse_args()
        text = "".join(args.expression)

        print_value(text)


if __name__ == "__main__":
    main()

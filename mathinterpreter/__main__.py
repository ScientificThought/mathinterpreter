import readline

from mathinterpreter.calculate import calc


def main():
    while True:

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

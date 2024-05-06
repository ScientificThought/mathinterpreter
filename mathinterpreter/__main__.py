from mathinterpreter.calculate import calculate


def main():
    while True:
        text = input("calc > ").strip()

        if text.isascii():
            text = text.lower()
            if text in ["q", "quit"]:
                break

        value = calculate(text)
        print(value)


if __name__ == "__main__":
    main()

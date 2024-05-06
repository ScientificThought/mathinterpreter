#from mathinterpreter.interpreter import Interpreter
#from mathinterpreter.lexer import Lexer
#from mathinterpreter.parser import Parser
from mathinterpreter.calculate import calculate


def main():
    while True:
        try:
            text = input("calc > ").strip()

            if text.isascii():
                text = text.lower()
                if text in ["q", "quit"]:
                    break

            value = calculate(text)
            print(value)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

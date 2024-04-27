from mathinterpreter.interpreter import Interpreter
from mathinterpreter.lexer import Lexer
from mathinterpreter.parser_ import Parser


def main():
    while True:
        try:
            text = input("calc > ").strip()

            if text.isascii():
                text = text.lower()
                if text in ["q", "quit"]:
                    break

            lexer = Lexer(text)
            tokens = lexer.generate_tokens()
            parser = Parser(tokens)
            tree = parser.parse()
            if not tree:
                continue
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            print(value)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

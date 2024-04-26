from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser

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

from mathinterpreter.interpreter import Interpreter
from mathinterpreter.lexer import Lexer
from mathinterpreter.parser import Parser


def calculate(text):
    try:
        if text.isascii():
            text = text.lower()
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree:
            return None
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        return value
    except Exception as e:
        print(e)



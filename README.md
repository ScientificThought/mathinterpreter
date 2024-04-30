# Python - Math Interpreter

An interpreter, written from scratch in Python, that can evaluate simple math calculations. This project is based on  [py-simple-math-interpreter](https://github.com/davidcallanan/py-simple-math-interpreter), by David Callanan and illustrates the use of software engineering techniques to evolve a prototype code into a  professional software. 

Since our objective is to create an education/professional example we don't change the original business logic, *i.e.*, the interpretor code is not changed and is kept with only addition, subtraction, multiplication, and division operations, as well as right and left parenthesis.

## How to install and run the REPL

Currently this package only contains a library and to install it you will need `git`, `pip`, and you will need to setup a Python virtual environment. There are many ways to do that but if you already know how to setup a virtual environment, probably you could proceed your way. 

If you are new to software development, follow the steps below:

Create a new directory and a new virtual environment for working with `mathinterpreter`:

```bash
mkdir mynewproject
cd mynewproject
python -m venv env
source env/bin/activate
```
After activating your new environment, install the package from source using pip:

```bash
python -m pip install git+https://github.com/ScientificThought/py-math-interpreter.git
```
At this point you can run the REPL, from the directory in which you installed the package by typing:

```bash
python mathinterpreter
```

This will open the REPL terminal of the  interpreter and you can it for typing math formula as follows:
```
❯ python mathinterpreter
calc > 1+1        
2.0
calc > (3.0+2*2)/3
2.3333333333333335
calc > 
```
Jus type `q` or `quit` followed by enter  in the REPL to return to your shell. That's it.

### How to use this package as Python module

For using the `mathinterpreter` as a library you will need to import the lexer, the parser, and the interpreter objects. For understanding how to and interpreter works it is recommended to look onto the file `matheinterpreter/__main__.py`, in which REPL is implemented. But the code below presents an snippet of how simple  and 'play' with technics for building and interpreter.

```python

from mathinterpreter.interpreter import Interpreter
from mathinterpreter.lexer import Lexer
from mathinterpreter.parser_ import Parser

text = '1 + 3*(5*2+1)/2'
tokens = Lexer(text).generate_tokens()
tree = Parser(tokens).parse()

interpreter = Interpreter()
value = interpreter.visit(tree)
print(value)
```

## What we have done and what we are doing

**Current implementation (2024.04.30) includes:**
- library `mathinterpreter` with it's subpackages;
- a single `pyproject.toml` to organize project;
    - installation using `pip`;
    - package build uses `setuptools`;
- tests using pytest.
- a simple simple REPL interface.

**Current goal is:**

Please check it out the issues, but we aim to implement:

- automated tests using GitHub Actions;
- linting with black, flake8 or ruff;
- expand the tests;
- improve the cli:
    - use argparse so that the user can call the interpreter from shell;
    - make the REPL more user friendly;
- create a documentation;
- test the documentation using doctests;

## Who we are?

We [Marco Barbosa](@aureliobarbosa) and [Henrique Guidi](@hsguidi), we both did PhD in Physics at University of São Paulo. ScientificThoughts was created as an online place to develop interesting projects while improving our software engineering techniques.
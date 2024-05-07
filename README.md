
![Static Badge](https://img.shields.io/badge/python-%3E%3D3.10-blue?style=flat&logo=python&logoColor=green&label=Python&color=green) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![Static Badge](https://img.shields.io/badge/unit_test-pytest-blue?style=flat&logo=pytest)

# Python - Math Interpreter

An interpreter, written from scratch in Python, that can evaluate simple math calculations, with a simple Read-Eval-Print-Loop (REPL) command line interface. This project is based on  [py-simple-math-interpreter](https://github.com/davidcallanan/py-simple-math-interpreter), by David Callanan and illustrates the use of software engineering techniques to evolve a prototype code into a professional software. 

Since our objective is to create an education/professional example we didn't change the original business logic, *i.e.*, the interpretor code is not changed and is kept with only addition, subtraction, multiplication, and division operations, as well as right and left parenthesis.

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
$ python mathinterpreter
calc > 1+1        
2.0
calc > (3.0+2*2)/3
2.3333333333333335
calc > q
$ 
```
Just type `q` or `quit` followed by enter  in the REPL to return to your shell. That's it.

### How to use this package as Python module

You can call `mathinterpreter` from your python code and use the function `calculate` to evaluate expressions, as in the following:
```python
from mathinterpreter import calc

value = calc('1 + 3*(5*2+1)/2')
print(value)
```
For using `mathinterpreter` as a library you will need to import the lexer, the parser, and the interpreter objects. For understanding how to and interpreter works it is recommended to look the files `mathinterpreter/__main__.py` and `mathinterpreter/calculate.py`, which implement the REP.

## What we have done and what we are doing

**Current implementation (2024.04.30) includes:**
- library `mathinterpreter` with it's subpackages;
- a single `pyproject.toml` to organize project;
    - installation using `pip`;
    - package build uses `setuptools`;
- tests using pytest.
- a simple simple REPL interface.
- automated tests using GitHub Actions;
- format code using with black;

**Current goal is:**

Please check it out the issues, but we aim to implement:

- add CI automation for black code formatter;
- implement code coverage;
- expand the tests suit;
- improve the cli:
    - use `argparse` so that the user can call `calculate` from shell and do useful work without leaving the terminal;
    - make the REPL more user friendly;

## Want to contribute

Please take a look on our [contributing guide](doc/guides/contributing.md).

## Who we are?

We are [Marco Barbosa](@aureliobarbosa) and [Henrique Guidi](@hsguidi), colleagues which got 
involved with computation while doing PhD in Physics at University of São Paulo. 

ScientificThoughts was created as an online place to develop interesting small projects to improving 
our software engineering techniques. Want to join us? Just contact us.
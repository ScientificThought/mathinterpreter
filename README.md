
![Static Badge](https://img.shields.io/badge/python-%3E%3D3.10-blue?style=flat&logo=python&logoColor=green&label=Python&color=green) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![Static Badge](https://img.shields.io/badge/unit_test-pytest-blue?style=flat&logo=pytest)

# mathinterpreter
## **An interpreter for evaluating simple math expressions.**

mathinterpreter evaluates simple math calculations through command line and console. This project is based on  [py-simple-math-interpreter](https://github.com/davidcallanan/py-simple-math-interpreter), by David Callanan, and illustrates the use of software engineering techniques to evolve a prototype code into a professional software.

Since our objective is to create an education/professional example we didn't change the original business logic, *i.e.*, we do not change the interpretor code. Besides the four basic operations ( addition, subtraction, multiplication, and division) we implemented the power operator `^` to calculate `a^b` and the modulo operator `%`.

## How to install and run the REPL

### Using pipx (recommended)

To use this project as a standalone command line tool install [pipx](https://pipx.pypa.io/stable/installation/) and run:

```bash
pipx install mathinterpreter
```
At this point you can run the console from anywhere in your machine by typing `mathinterpreter` in your terminal console. 
This will open the console terminal of the interpreter and you can now use it for evaluating math expressions:
```
$ mathinterpreter
calc > 1+1        
2.0
calc > (3.0+2*2)/3
2.3333333333333335
calc > q
$ 
```
Just type `q` or `quit` followed by enter in the console to return to your shell. 

Alternatively you can also provide math expressions as parameters to `mathinterpreter`, as described below:
```
$ mathinterpreter 1+1
2.0
$ mathinterpreter "1 + 1"
2.0
$ 
```
For more examples, use `mathinterpreter -h`. That's it.


### Install using pip

If you want to install this package and use it as a library on another project you can use `pip` and a virtual environment manager.  There are many ways to do that but if you already know how to setup a virtual environment, probably you could proceed your way. 

In our development setup we use `venv`, which comes with python, on Ubuntu Linux. If you are new to software development, follow the steps we recommend below which is expect to work on any Linux Distribution.

Create a new directory and a new virtual environment for working with `mathinterpreter`:

```bash
mkdir mynewproject
cd mynewproject
python -m venv env
source env/bin/activate
```
Note that `mynewproject` could be any name of your choice and that instead of using `source` you could simply use the `.` command. After activating your new environment, install the package from source using pip:

```bash
python -m pip install mathinterpreter
```
Through this procedure you can run `mathinterpreter` inside the virtual environment you just created and import 
`mathinterpreter` as a library to use in your project, as we discuss below.


### How to use this package as Python module

You can import the module `mathinterpreter` from your python code and use the function `calc` to evaluate expressions, as in the following:
```python
from mathinterpreter import calc

value = calc('1 + 3*(5*2+1)/2')
print(value)
```
To using `mathinterpreter` as a library you will need to import the Lexer, the Parser, and the Interpreter classes. 
For understanding how the interpreter works we recommend you to look the files `mathinterpreter/__main__.py` and `mathinterpreter/calculate.py`, which implement the Read-Eval-Print-Loop (REPL) console.

## Who we are?

We are [Marco Barbosa](@aureliobarbosa) and [Henrique Guidi](@hsguidi), colleagues which got 
involved with computation while doing PhD in Physics at University of São Paulo. 

ScientificThoughts was created as an online place to develop interesting small projects to improving 
our software engineering techniques. Want to join us? Just contact us.

## Contributing

This project was created to showcase how to improve a simple project using software engineering techniques. If you have questions or want to collaborate with us in other related projects, contact us preferencially through Linkedin. Our contacts also can be found in our personal GitHub profiles.

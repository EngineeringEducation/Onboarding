Exercise 03: Interfaces, main loops revisited
=======

Introduction
--------
As we saw before, a main loop looks like this:
```python
do_setup()
while exit_condition_not_reached:
    input = consume_input()
    output = evaluate_input(input)
    print output
```
When we consume input from the keyboard, this is a special type of main loop called a 'REPL', a read-eval-print-loop.

In [Guessing Game](../guessing_game), we built a very simple REPL that asked for a single number from the user.

In [calculator](../calculator), we provided a REPL for you that implemented a basic calculator.

In this exercise, you will re-implement the same REPL from scratch. To do this, you will need to tokenize a string.

Tokenizing a string is the process of taking a string and breaking it up into its constituent parts as a list. Consider the following string:

    ocean_animals = "shark,squid,tuna,flounder"

A natural tokenization would be the following array:

    ["shark", "squid", "tuna", "flounder"]

To do this, we use the string split method:

    ocean_animals.split(",")
        => ["shark", "squid", "tuna", "flounder"]

When we do this, we say we've tokenized the original string on commas.

Now consider the following string as read from the keyboard:
```python
input = "pow 3 5"
```
If we tokenize on spaces, we get the following list:
```python
tokens = input.split(" ")
# tokens = ["pow", "3", "5"]
```
Now, we can take the first token, token[0], and make a decision about what to do with the remaining tokens. For example:

    if tokens[0] is equal to "pow":
        call the power function with the other two tokens

The psuedocode for our REPL will look like this:

    # No setup
    repeat forever:
        read input
        tokenize input
        if the first token is 'q', quit
        otherwise decide which math function to call based on the tokens we read


##### Look at these if you need them:

* http://learnpythonthehardway.org/book/ex3.html
* http://learnpythonthehardway.org/book/ex18.html
* http://learnpythonthehardway.org/book/ex19.html
* http://learnpythonthehardway.org/book/ex21.html
* http://learnpythonthehardway.org/book/ex29.html
* http://learnpythonthehardway.org/book/ex30.html
* http://learnpythonthehardway.org/book/ex31.html
* http://www.learnpython.org/en/Variables_and_Types
* http://www.learnpython.org/en/Functions
* http://docs.python.org/library/functions.html#int

##### Concepts required:
* functions
* arithmetic
* return values
* string parsing
* conditionals

Description
-------
Now that we've finished our aritmetic functions in [calculator](../calculator), we're going to implement the calculation portion ourselves. You will eventually need to copy your arithmetic.py file from [calculator](../calculator) as you implement your own version, but you can use the one provided for now if you like. Do this exercise in the same directory so you get practice with pushing updates to repos. Now is an ideal time to learn Branching, so type `git checkout -b add-calculation-implementation`.

Implement a REPL for a calculator in a file named 'calculator.py'. Your calculator will use the interface from the previous exercise:

    In the file arithmetic.py, these function signatures are required

    add(int, int) -> int
    Returns the sum of the two input integers

    subtract(int, int) -> int
    Returns the second number subtracted from the first

    multiply(int, int) -> int
    Multiplies the two inputs together

    divide(int, int) -> float
    Divides the first input by the second, returning a floating point

    square(int) -> int
    Returns the square of the input

    cube(int) -> int
    Returns the cube of the input

    power(int, int) -> int
    Raises the first integer to the power of the second integer and returns the value.

    mod(int, int) -> int
    Returns the remainder when the first integer is divided by the second integer.


A sample session of the calculator looks like this:
```    
Meringue:math chriszf$ python calculator.py
> + 1 2
3
> - 10 5
5
> * 2 3
6
> / 7 2
3.500000
> square 2
4
> cube 3
27
> pow 2 5
32
> mod 10 3
1
> q
Meringue:math lizthedeveloper$
```
We have provided a sample arithmetic.py with dummy stubs that do the wrong thing. When you've completed your REPL, copy your completed arithmetic.py from the previous exercise to the current directory and replace our stubs.

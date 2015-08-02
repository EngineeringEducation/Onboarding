# Python

## Notes
The python version we're going to standardize on is Python 2.7 - this is because it's simpler to learn and use than Python 3, and there are a large number of libraries that still do not support Python 3. We'll switch over when all of the major data analysis libraries and Flask switches over to Python 3. [Here's some thoughts from the authors of Flask about it](http://flask.pocoo.org/docs/0.10/python3/).

## Pre-work
If you don't have any experience with Python at all, the first place to start is [Learn Python The Hard Way](http://learnpythonthehardway.org/book/).

* Get comfortable with the syntax of Python with exercises [0](http://learnpythonthehardway.org/book/ex0.html) through [39](http://learnpythonthehardway.org/book/ex39.html)
* Take a tour of Object Oriented Python with exercise [40](http://learnpythonthehardway.org/book/ex40.html), [41](http://learnpythonthehardway.org/book/ex41.html), and [42](http://learnpythonthehardway.org/book/ex42.html)
* Understand Inheritance with exercise [44](http://learnpythonthehardway.org/book/ex44.html)[^1].

## Python Resources


* [The Python 2.7 Docs](https://docs.python.org/2.7/)
* [A Project Skeleton](http://learnpythonthehardway.org/book/ex46.html) - a guide to starting a Python project by Zed Shaw
* [A Flask Starter Project](https://github.com/TradecraftEngineering/flask-starter) - something you can clone and start immediately
* [A great Python Cheatsheet](http://overapi.com/python/)



## Beginner Exercises

### Syntax
* [Guessing Game](/guessing_game)
* [Calculator - Part One](/calculator)
* [Calculator - Part Two](/calculator_2)
* [List Operations](/list_operations)
* [Data Structures](/data_structures)
* [State and Traversal](/counts_and_traversal)
* [Extra Data Structures](/data_structures_2)

## Advanced Exercises
* [Python Review](/experienced_python_users_review) - For people with some python experience already
* [Markov Chains](/markov_chains) - test your basic algorithmic thinking




[^1] The author has a lot of opinions here about inheritance, which I endorse. Try to stay away from too much abstraction in Python, as it's meant to be simple and readable, and inheritence tends to really needlessly complexify programs that are pretty simple.
List Operations
==============

### A few things about lists

First, work through the following resources on lists:

* http://learnpythonthehardway.org/book/ex32.html
* http://learnpythonthehardway.org/book/ex33.html
* http://learnpythonthehardway.org/book/ex34.html
* http://learnpythonthehardway.org/book/ex38.html
* http://learnpython.org/en/Lists
* http://docs.python.org/tutorial/introduction.html#lists
* http://docs.python.org/tutorial/datastructures.html#more-on-lists
        --> stop reading before section 5.1.1

### A few things about tests

#### Some background reading (just read, don't do):

http://learnpythonthehardway.org/book/ex47.html

#### What's going on here?

In this exercise directory there are two files: `list_operations.py` and
`test_list_operations.py`.

`list_operations.py` contains lots of empty functions that take an input list and don't do anything.    
`test_list_operations.py` contains lots of full functions that ... ? Well, let's find out.

####Try it out!

Try running `python test_list_operations.py` at the CLI prompt. You should see a lot of console output that ends with the following text:
```
----------------------------------------------------------------------
Ran 25 tests in 0.007s

FAILED (failures=25)
```

Wow, 25 failures. That doesn't sound good. What just happened?


Well, `test_list_operations.py` just ran 25 'tests' on `list_operations.py` and none of them worked. How did it do that?

####What's a test?

Each function in `test_list_operations.py` (which I will now refer to as a test) does four things:    
1. Gets some sample data (initialized in `setUp()` and passed in to each function with `self` -- more on this on a later date)    
2. Sends the sample data through a `list_operations.py` function (there's one test function for each regular function)    
3. Defines what the correct output for each function should be based on the input    
4. Tests whether the result of the `list_operations.py` function matches the expected input ( it asserts equality )    

If all of the asserted equality turns out true, then your test passes. If any of them fails, your test fails.    
All of your tests failed because, obviously, there's nothing in any of your `list_operation` functions. So whatever your function returns (it returns nothing) doesn't match what the test expects (very specific things, including not nothing).

For example: `test_1_A_head()` checks the function `head()` in `list_operations.py`. It asserts that the result of calling the function `head()` with the test data `months` should result in `'Jan'`.

One thing to note is that `test_1_A_head()` is laid out differently than a test like `test_1_J_replace_head()`. The latter calls the function first, then checks the result in a different step. **This is important!** Why?

When a test fails, it will print the un-matching-ness in the terminal. This may be helpful for troubleshooting your list operators. Also, sometimes you may see something like:
```
FAILED (failures=24, errors=1)
```
Don't get too excited that your failure number has gone down by one -- an error means that the function call errored out when the test called it. You'll be able to see the error message it returned if you scroll up in the terminal to that test's section.

### Go!

Your mission is to get all the tests to pass by actually writing the functions in `list_operations.py`. When you've succeeded, you'll see only this output when you run your tests: 
```
.........................
----------------------------------------------------------------------
Ran 25 tests in 0.002s

OK
```
#### Part 1: Fundamental operations on lists

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
* List literals (`[]`, `['hello']`, `[3, 1, 4, 1, 5, 9]`, etc.)
* List indexing (`some_list[index]`)
* List indexing assignment (`some_list[index] = value`)
* List slicing (`some_list[start:end]`)
* List slicing assignment (`some_list[start:end] = another_list`)
* List index deletion (`del some_list[index]`)
* List slicing deletion (`del some_list[start:end]`)

In this section you will implement functions that each use just one of the above
operations. The docstring of each function describes what it should do. Consult
`test_list_operations.py` for concrete examples of the expected function behavior.

**DO NOT USE ANY OF THE BUILT IN LIST METHODS**

**DO NOT USE `len(l)`**

**GET A CODE REVIEW BEFORE MOVING ON TO PART 2**

#### Part 2: Derived operations on lists

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 and 2 in your implementations.
For loops are also allowed, such as the following:
```    
for element in some_list:
    # Do something with element
```
Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.

**Don't forget to get a code review when you think you're finished**

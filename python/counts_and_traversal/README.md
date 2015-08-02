Exercise 05: Files, Creative uses of lists
==========================================

Introduction
------------
Files can be opened using the .open method, and then processed one character at a time as a bytestream using the .read method with an argument of 1:
```python
f = open("myfile.txt")
firstletter = f.read(1)
f.close()
```
The entire file can be read in all at once using the .read method with no arguments:
```python
f = open("myfile.txt")
filetext = f.read()
f.close()
```
Once a file has been read, it can be iterated through as if it were a list:
```python
# Print one character at a time to the screen
    for char in filetext:
        print char
```
##### Do These First:
* http://learnpythonthehardway.org/book/ex15.html
* http://learnpythonthehardway.org/book/ex16.html
* http://learnpythonthehardway.org/book/ex17.html
* http://www.asciitable.com/
* http://docs.python.org/library/functions.html#ord

##### Useful Concepts:
* string.lower()
* ord()

Problem Description
-------------------
Write a program, lettercount.py, that opens a file named on the command line and counts how many times each letter occurs in that file. Your program should then print those counts to the screen, in alphabetical order. For example:

    inputfile.txt:
    An abacus

    $ python lettercount.py inputfile.txt
    3
    1
    1
    0
    0
    ...

We have provided a file 'twain.txt' for you to test your code on.

Extra Credit
-------

Once you've produced appropriate output, you can visualize it by piping the contents of your program to the 'spark' utility installed on your computer:

    $ python lettercount.py inputfile.txt | spark
    ▃▂▄▁▇▅█▁▇▂▁▁▅▃▅▇▁▄▄▂▂▇▆▄▂▄




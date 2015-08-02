Project 1: Looping, file manipulation, panic
=======

Introduction
-------

Resources:
* http://learnpythonthehardway.org/book/ex32.html
* http://learnpythonthehardway.org/book/ex34.html
* http://www.learnpython.org/en/Lists
* http://www.learnpython.org/en/Loops
* http://www.learnpython.org/en/Basic_String_Operations
* http://docs.python.org/library/os.html#os.listdir
* http://docs.python.org/library/os.html#os.chdir
* http://docs.python.org/library/os.path.html#os.path.exists
* http://docs.python.org/library/shutil.html#shutil.move

Concepts required:
* for loops
* conditionals
* lists
* paths
* substrings

Description
-------
Included in the exercise is a zipfile, 'files.zip'. It contains 200 files with random character strings for names, all lowercase. First, unzip this file into a directory named 'original_files'.

Your job is to write a program, ex1.py, that does the following things:

1. Create 26 directories in the current directory, one for each letter of the alphabet:
    ./a/
    ./b/
    ./c/
    etc.

2. Loop through all the files in the original_files directory, and organize each of those files into the directory that their name starts with.

### Example:
    The file named 'artichoke.txt' would go into the directory 'a',
    'bartholomew.txt' would go into 'b'.

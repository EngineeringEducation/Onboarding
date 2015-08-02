Exercise 7: Files and dicts
============================

Introduction
------------

You may find the following methods useful:
```python
string.split()
string.strip()
dict.get()
dict.iteritems()
```

Problem Description
-------------------

Write a program, wordcount.py, that opens a file named on the command
line and counts how many times each space-separated word occurs in
that file. Your program should then print those counts to the
screen. For example:

inputfile.txt:
```
As I was going to St. Ives
I met a man with seven wives
Every wife had seven sacks
Every sack had seven cats
Every cat had seven kits
Kits, cats, sacks, wives.
How many were going to St. Ives?
```
Example output:
```
$ python wordcount.py inputfile.txt
seven 4
Kits, 1
sack 1
As 1
kits 1
Ives? 1
How 1
St. 2
had 3
sacks, 1
to 2
going 2
was 1
cats, 1
wives 1
met 1
Every 3
with 1
man 1
a 1
wife 1
I 2
many 1
cat 1
Ives 1
sacks 1
wives. 1
were 1
cats 1
```

We have provided a file 'twain.txt' for you to test your code on.

Extra Credit
-----------
The output of your program is not as nice as it could be. Try to improve it:

* Some words are counted separately due to punctuation. Remove punctuation so that they appear as the same word in the output.
* In the example above, 'Kits' and 'kits' are treated separately because they have different capitalization. Make all words lowercase so that capitalization doesn't matter.
* Sort the output from the highest frequency words to the lowest frequency words.
* Sort words having the same frequency alphabetically.


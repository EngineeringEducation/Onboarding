Exercise 06: Files and dictionaries
=======

##Dictionaries

###What is a dictionary?

Imagine a list as being a numbered sequence of data.
```python
fish = ["shark", "ray", "halibut", "tuna", "squid"]
```
The first element is shark, and you access it by its index number:
```
print fish[0]
=> shark
```
To access the nth element, its index number is n-1. The fifth element is accessed thusly:
```
print fish[4]
=> squid
```
What if, instead of a numbered index, we could use a string as an index?
```
print fish["deep ocean"]
=> anglerfish
print fish["shallow river"]
=> candiru
```
We would then need another way of specifying a list where each element is named.
```python
fish = {"deep ocean": "anglerfish", "amazon river": "candiru", "lake": "bass", "shallow river": "trout"}
```

This is called a dictionary in python. It's also called a hashtable, or a hashmap, or very non-specifically, a map. __A dictionary is a collection of 'key-value pairs'__. The key 'deep ocean' _maps_ to the value 'anglerfish'.

###Why use a dictionary?
Imagine you were writing a program to keep track of user scores in a game. If you only had arrays, you might do something like this:
```
names  = ["Bob", "Joe", "Jack", "Jane"]
scores = [   10,     3,      6,     15]
```
To find Joe's score, first you'd have to find which position "Joe" is in, then use that position to look up his score.
```
index_joe = names.index("Joe")
print "Joe's score is %d" % (scores[index_joe])
=> Joe's score is 3
```
This is unwieldy and complicated. With dictionaries, we could instead do the following:
```python
scores = {"Bob": 10, "Joe": 3, "Jack": 6, "Jane": 15}
```
```
print "Joe's score is %d" % (scores['Joe'])
=> Joe's score is 3
```

###Some useful methods:
####get()
Dictionaries have a method called 'get' which allows you to have a default value in case a key does not exist beforehand.
```
scores = {"Bob": 10, "Joe": 3, "Jack": 6, "Jane": 15}

print scores.get("Bob", 0) # The second argument is the fallback number if the key doesn't exist
=> 10

print scores.get("Billy", 0) # Billy doesn't exist in the dictionary, so return the fallback instead
=> 0
```

####iteritems()
Dictionaries can also be iterated entry-by-entry, using the method ```iteritems()```.

For example:
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.iteritems():
    print "Key == %r, value == %r" % (key, value)
```
Prints:
```
Key == 'a', value == 1
Key == 'b', value == 2
Key == 'c', value == 3
```
This introduces two loop variables, 'key' and 'value', that will store the key
and value elements of each dictionary entry in turn.


###Dictionary Exercises (do these first):
* http://learnpythonthehardway.org/book/ex39.html **(Stop at "Making Your Own Dictionary Modules")**
* http://docs.python.org/tutorial/datastructures.html#dictionaries
* http://www.learnpython.org/en/Dictionaries
* http://docs.python.org/library/stdtypes.html#mapping-types-dict (Read. Familiarize, not memorize.)




##File Parsing

###Read lines from a file
In exercise 5 you read a file and processed one character at a time. Files can also be iterated line-by-line, using a for loop on the file directly.

For example:
```python
twain = open('twain.txt')
for line in twain:
    # Do something
```
The loop variable ```line``` will store each line of the file in turn.

### File manipulation Exercises (and sometimes strings):
* http://learnpythonthehardway.org/book/ex15.html
* http://learnpythonthehardway.org/book/ex16.html
* http://learnpythonthehardway.org/book/ex17.html
* http://docs.python.org/tutorial/inputoutput.html#methods-of-file-objects
* http://docs.python.org/library/stdtypes.html#string-methods
* http://stackoverflow.com/a/3437070





Codin' time
-------
In this directory, you will find a text file, ```scores.txt```, containing a series of local restaurant ratings. Each line looks like this:
```
Restaurant Name:Rating
```
Your job is to write a program named ```'sorted_data.py'``` that reads the file, then spits out the ratings in alphabetical order by restaurant.

Sample output:
```
Meringue:Exercise07 chriszf$ python sorted_data.py
Restaurant 'Andalu' is rated at 3.
Restaurant "Arinell's" is rated at 4.
Restaurant 'Bay Blend Coffee and Tea' is rated at 3.
Restaurant 'Casa Thai' is rated at 2.
Restaurant 'Charanga' is rated at 3.
Restaurant 'El Toro' is rated at 5.
Restaurant 'Giordano Bros' is rated at 2.
Restaurant "Irma's Pampanga" is rated at 5.
Restaurant 'Little Baobab' is rated at 1.
Restaurant 'Pancho Villa' is rated at 3.
Restaurant 'Taqueria Cancun' is rated at 2.
Restaurant 'Urbun Burger' is rated at 1.
```
When you're finished, please get a code review from one of your friendly neighborhood instructors/TAs.  

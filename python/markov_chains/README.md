Exercise 08: Markov Chains (Hint: the answer is dictionaries)
=======

Introduction
-------
A Markov chain is a sequence of random variables X1, X2, X3, etc., with the property that the present, past, and future states are independent. Formally,
```
Pr(Xn+1 = x|X1 = x1, X2 = x2, ... , Xn = xn) = Pr(Xn+1 = x|Xn = xn)
```
Just kidding, that's a terrible explanation. 

Colloquially, Markov chains are a statistical analysis of frequency patterns in some sequence. Consider the following sequence of words:
```
Would you, could you in a house
Would you, could you with a mouse
Would you, could you in a box
Would you, could you with a fox
Would you like green eggs and ham?
Would you like them, Sam I Am?
```
There is a high frequency of repetition here, and if we were trying to generate a new, unique verse to follow this one, we might just analyze the text for the most common words, and randomly choose from them:
```
You! Could a box? With you in eggs.
```
This isn't completely out of place, but it's not exactly 'right' either. Obviously there's more to the pattern. Let's change our analysis to determine the frequencies of word pairs, as opposed to single words:
```
Would you
you could
could you
you in
in a
a box.
```

Now, choosing from these pairs produces something slightly better:
```
Would you? You could! In a... a box.
```
Again, better, but not great. Let's change our analysis a little bit, and the rules for choosing besides. Instead of word pairs, we produce a list of every word, and the chance that it's followed by the next word in the text:
```
would -> you (100%)
you -> could (40%), like (20%), in (20%), with (20%)
could -> you (100%)
like -> green (50%), them (50%)

... and so forth ...
```
Instead of just choosing a random pair, we start by choosing a random word on the left, and choose a word on the right to follow according to the weight. After choosing a word from the right, you can repeat the process, using the word from the right and looking it up on the left, repeating ad nauseum.
```
Would you in a fox? Could you like green eggs. 
```
We can improve things even further by using word pairs on the left of the arrow, instead of single words:
```
would you -> could (66%), like (33%)
you could -> you (100%)
could you -> in (50%), with (50%)
you in -> a (100%)
you with -> a (100%)
in a -> house (50%), box (50%)
with a -> fox (50%), mouse (50%)
you like -> them (50%), green (50%)
```
Following the same process, again, choosing a word pair from the left, then randomly choosing a successor from the right, according to the weight:
```
You could. You, with a fox! Would you like them?
```
The longer the sequence of words to the left of the arrow, the closer it becomes to the original text, as well as valid English, because there are fewer and fewer random successors. Here, we use bigrams (word pairs) and a successor, but we could use trigrams or n-grams (sequences of n words). The longer the n-gram, the closer you get to the source corpus.

Let's look at this again, using Britney Spears' hit song, Womanizer, as the source corpus.
```
womanizer womanizer -> womanizer (100%)
```
And the resultant text:
```
WOMANIZER WOMANIZER WOMANIZER WOMANIZER WOMANIZER WOMANIZER 
WOMANIZER WOMANIZER WOMANIZER WOMANIZER WOMANIZER WOMANIZER 
WOMANIZER WOMANIZER WOMANIZER WOMANIZER WOMANIZER WOMANIZER
```
If only there were some data structure we could use to contain all of these chains which MAP word pairs to some LIST of values... fine, you've twisted my arm.
```
{ ("womanizer", "womanizer"): ["womanizer"] }
```
**Notice here, we're explicitly nesting data structures, using a tuple as a key in a dictionary, and a list as the value.**
*Emphasis added to see if you've read this far because this part might be important*


Description
-----------
You are to produce a random text generator using markov chains. We've provided a very bare skeleton for you to start your program from. Up until now, we've been writing our programs in a very freeform manner, just writing code at the 'top level', the same place where we put our global variables. This is generally considered bad form. Code should always be contained in functions or class methods wherever possible.

The skeleton program we've provided has a recommended set of functions to start with, including a very odd if statement at the bottom. You can ignore how this statement works for now, all it does is it makes sure your program starts inside the ```main()``` function.

The program should accept a filename from the command line, and a sample run should look similar to the following:
```
meringue:Exercise08 chriszf$ python markov.py shakespeare.txt
Forsooth, or somesuch.
```
You can use any text as an input corpus, you might try [Project Gutenberg](http://www.gutenberg.org/) for some inspiration.

Once you've got your random text generator working to a somewhat sensible point, you're finished! Please pause, and procure a code review. Then, read below for more challenges.

Extra Credit
------------
Do any of the following

1. See what happens when you mix two different authors together as a single source
2. Modify the program to allow any number of words to use as keys, ie: choose the size of your n-gram used in your chain
3. Create a new Twitter persona and wire up your markov program with the twitter module (import twitter) to produce random tweets. (docs are [here](https://code.google.com/p/python-twitter/)). The twitter module is already installed on the lab machines. NOTE: Do not publish your Twitter API credentials to GitHub! Create a file with your credentials and then make Git ignore it with .gitignore 

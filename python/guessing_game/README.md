Exercise 01: Conditionals, variables
=======

Tutorials & Resources:
-------
Take a look at these if you haven't yet, or if you aren't sure where you start on the exercise.

* [Strings](http://learnpythonthehardway.org/book/ex6.html)
* [Printing](http://learnpythonthehardway.org/book/ex7.html)
* [Input](http://learnpythonthehardway.org/book/ex11.html)
* [If Statements](http://learnpythonthehardway.org/book/ex29.html)
* [Else](http://learnpythonthehardway.org/book/ex30.html)
* [Elif](http://learnpythonthehardway.org/book/ex31.html)
* [While Loops](http://learnpythonthehardway.org/book/ex33.html)
* [Loops](http://learnpython.org/en/Loops)
* [Functions](https://docs.python.org/2/library/functions.html#int)

Concepts required:
* while loops
* 'break' statement
* conditionals
* user input
* formatting strings
* the int() function

Introduction
-------
Programs tend to be structured around a 'main loop', which repeatedly executes the primary task of the program. It is important to understand that the primary task is not necessarily the primary function of the program. As an example, the primary function (or at least, the primary usage) of the program 'cat' is to print the contents of a file to the screen. However, the primary task in accomplishing that is printing individual lines of the file in sequence. In pseudocode, it might look like this:

    f = open_file(filename)
    for each line 'l' in file 'f':
        print l

Consider a calculator program, that lets you enter arithmetic expressions, then evaluates and prints the output until you tell it to quit. It might look like this:

    while True:
        expression = read_input()
        value = evaluate_expression(expression)
        print value

In general, a program is structured like this:

    do_setup()
    while exit_condition_not_reached:
        input = consume_input()
        output = evaluate_input(input)
        print output

In the case of 'cat', input comes from the file specified on the command line. In the calculator, input comes from the keyboard.


Description
-------
Write a program named guess.py that plays the 'number guessing game'. The computer will choose a random number between 1 and 100, and ask the user to guess the number, giving them a hint if it's high or low. A sample game looks like this:

```
Meringue:guessing lizthedeveloper$ python ./guess.py
Howdy, what's your name?
(type in your name) Liz
Liz, I'm thinking of a number between 1 and 100. Try to guess my number.
Your guess? 50
Your guess is too low, try again.
Your guess? 80
Your guess is too high, try again.
Your guess? 60
Your guess is too low, try again.
Your guess? 70
Your guess is too high, try again.
Your guess? 63
Your guess is too low, try again.
Your guess? 64
Your guess is too low, try again.
Your guess? 67
Your guess is too low, try again.
Your guess? 69
Your guess is too high, try again.
Your guess? 68
Well done, Liz! You found my number in 9 tries!
```

A rough pseudocode outline of the program will look like this:

    greet player
    get player name
    choose random number between 1 and 100
    while True:
        get guess
        if guess is incorrect:
            give hint
        else:
            congratulate player

Version Control (git)
-------
While you're writing your code, try and remember to use 'git' at various points to save your progress.  If you've never used version control before, it's a lot like enabling "Track Changes" in a Microsoft Word document.  Every time you "commit" your code, you're saving a snapshot in time.  If you make a change you don't like or mess something up, you can rollback to a previous commit.

For those of you who play adventure games, the motto "Save Early, Save Often" should come to mind.

So if you take the rough pseudocode outline from above, you'll probably want to go about creating your program in the following order:

1. Create a new folder/directory to store your project
1. Create your project file.  "subl guessing.py" will probably get you started.  ;)
1. Have your code greet the player.
1. Test your code!  Does it greet the player?
1. Time to save!
  1. git init
  1. git status
  1. git add guessing.py
  1. git status
  1. git commit -a -m "Greeting the Player"
  1. git status
  1. git log
1. Ok, on to the next step!  Get the player's name.
1. Test your code!
1. Does it work?  Time to save!
  1. git status
  1. git commit -a -m "Getting the Player's Name"
  1. git status
  1. git log
1. Sensing a pattern yet?  Repeat for the next steps, testing your code at each step.  When you have a step working, save it!

As you get more comfortable with git, you won't need to do a 'git status' at every step.  We're only having you do that here so you can see what is happening at each step and get used to the messages that git returns.

## Go Back!
At some point, commit your working code as is, and then go ahead and break something. Yes, make something stop working. And then save, but do NOT commit, these changes. Once you've wreaked some amount of havoc, continue reading. 

Often, you will explore an idea that didn't turn out the way you wanted it to, or accidental changes get saved. In these cases, you'll just want to go back to your last commit, and throw out the changes you've made. Try:

    git reset --hard

*WARNING:* This will erase any changes you have not committed to git, so please use with care!




Extra Credit
-------

Make your program a little more user friendly:

1. If the user inputs something that is not a number, mock them for their crimes and ask them to enter a valid number.
2. If the user inputs a number that isn't between 1-100 as requested, mock them for their crimes and ask them to enter a valid number.
3. Ask the user if they would like to play again and restart the game rather than exiting.
4. Keep track of the "high score" (or is that low score?) and display that when you congratulate the user

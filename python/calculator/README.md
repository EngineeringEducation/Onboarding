Exercise 02: Math and functions
=======

Introduction
--------
We're taught mathematical notation using 'infix' notation, that is, the operator goes between the numbers:

    eg: In '3 + 2', the operator, '+', goes between the operands, 3 and 2.

An alternate notation for math is called 'prefix'. As you might have guessed, in prefix notation, the operator goes in front of the operands:

    eg: In prefix notation, the same statement would be written '+ 3 2'

Some advantages of prefix notation include the ability to have an arbitrary number of operands.

    eg: '+ 3 2 1 4 5 6 7' will add up all the numbers.

In this exercise, we will build a basic prefix calculator together. We will provide half of the program, and you will code the other half. We will use this idea to explore the concept of an 'interface'.

In common English, an interface is defined as a surface that is a common boundary between two different things. In computing, the idea is very similar. An interface is the common 'surface' between two pieces of code, and is defined by an agreed-upon set of 'function signatures'.

A function signature is a way of describing a function without going into the details of how it operates. For example, consider the following function:

    def square(x):
        return x * x

If we were to describe this function, we might say "the function named 'square' accepts a single number as an input, and returns a number as output (presumably the square of the input)." This phrase is the function signature. It includes the function name, the number (and type) of inputs, and the type of the output. We can also include a rough description of what the function is _supposed_ to do. More succinctly, we can say:

    square(int) -> int
    Returns the square of the input integer.


Note that it says nothing about how the output integer is produced, nor does it say anything about the correctness of the output. It also doesn't say anything about what arguments to a function should be named.

Why is this useful? Well, when two or more programmers collaborate on a project, it is rare that they can work completely independently of each other. At some point, I will rely on code that you have written, or more likely, you will write in the future. If I waited until you wrote your code, that would delay the project significantly. Instead, we would agree upon an interface, a series of method signatures that my code would use to interact with yours. I would write my code _assuming_ at some point, you will fill in those method signatures with the correct implementation eventually.

One way of thinking about it is like after-market parts for cars. As long as the screws and holes are in the right positions at the right sizes, the pieces can be bolted together even though they come from different manufacturers.


##### Do These first:

* http://learnpythonthehardway.org/book/ex3.html
* http://learnpythonthehardway.org/book/ex18.html
* http://learnpythonthehardway.org/book/ex19.html
* http://learnpythonthehardway.org/book/ex21.html
* http://www.learnpython.org/en/Variables_and_Types
* http://www.learnpython.org/en/Functions

##### Concepts required:
* functions
* arithmetic
* return values


Description
-------
We have provided a program, calculator.pyc that implements a basic prefix calculator.  To download the file from github, click on the file, then click on "Raw" to download the file (the browser may place it in your Downloads folder). You will also need arithmetic.py. To download it, click on the filename above, then click "Raw". Then just do File->Save Page As in Chrome and put it in your project directory (i.e. don't work in your Downloads directory). You need both files in the same place to do this exercise.

A pyc is a special python file.  It's python code that has been "compiled" into machine code. You can still run the program, but you can't view the original source of the program.  If you try and look at the file on your terminal (e.g. "cat calculator.pyc") you probably get a bunch of gross garbage outputted.  That's okay, because the computer still knows how to run it.

As you create and run more python programs, you may notice .pyc files get created.  That's fine, they're making things run faster.  However they're not your source code and you probably don't want to check them into version control (git).

Run it with the following command from your shell:

    python calculator.pyc

The calculator lets a user add, subtract, multiply, divide, square a number, cube a number, and find the square root.

Calculator uses the following interface:

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

    Meringue:math chriszf$ python calculator.pyc
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
    Meringue:math chriszf$ 

We have provided a sample arithmetic.py with a function that matches the signature for 'add', although it returns an incorrect value. Your job is to make it return the correct value, then provide the remaining interface.

Try running the program first to understand where and how it fails. Read the error messages, and try to fix it by addressing one error at a time.

**Once you have finished all the functions, call an instructor over for a code review.**


Version Control
-------
Just like in [Guessing Game](../guessing_game) we want to make sure we're saving our work along the way.  Start getting used to creating a new git repo, we'll be doing it for each project we do.

In short, remember this pattern:

1. Create a new directory for your project
2. Run 'git init' to create the git repository
3. Write some code
4. Test some code
5. Got something working / at a good place to save?  'git add' to add your changes.
6. 'git commit' to save what you've added.  Nothing is saved until you commit
7. Goto Step 3

As you write the code for the functions in arithmetic.py, test one and then commit the change to git before moving on to the next one.  It may seem a little like overkill at this point since these functions are so small, but this is a habit you'll want to start practising.

Complete this exercise before moving onto the next section.

## Share and Share Alike

git is great and all, but so far everything you've commited has only been saved on the computer you've been working on.  If you move to another workstation or want to work on your computer at home, the files are not there.

Enter "[github](http://github.com)" to save the day!

Github is a company that offers a remote place to syncronize your repository.  This makes it easy to keep multiple machines up to date.  As you've already seen, you don't need github to use git, but it does make things easier.

If you have not yet created a github account, make sure you and your partner have done that now.

Log into your github account and find the "Create Repository" button to create a place in github.  Under "Repository Name", enter `calculator` (or whatever you'd like call it, but note this affects the URL). The description is optional. Leave it set to Public, because Private repositories cost money. Don't check "initialize this repository with a README" because you've already initialized the repository on your local machine with "git init".  Click "Create Repository".

You'll see a screen that says "Quick Setup" - click the SSH button. You'll see an address that says something like git@github.com:TradecraftEngineering/Onboarding.git - copy this url. This is the address of the remote (called so because it's on a different server) git repository we're going to add to our local repository.

Now you want to tell your local git repository about this new remote source.  When you add the remote source, you also give it an identifiable name that you use to refer to it.  Usually you would use the name "origin" as that's the default name.  However, because you're pairing with another student to work on these exercises, you'll be adding two remotes to each of your projects, so it makes more sense to use your username (no spaces!) to identify the remotes.  To add the remote to your repository:

    git remote add [your username goes here] git@github.com:[your username goes here]/[repo name goes here].git/

When we add a remote, much like when we do any other configuration, it only exists for that repository. Outside of the folder our repository is in, none of these settings exist. 

Now we have a remote - this is like a portal that goes to whatever URL we point at.  So, now that we've established a portal link, what do we do with it? Same thing you'd probably do if you actually opened a portal to the server room at Github. Push things through it and see what happens.

    git push [remote name] master

Replace \[remote name\] (no square brackets) with the name you used when you added the remote.  You might wonder about what "master" means - that's the name of the branch. For now, we'll have only one branch, so we'll always type master there. In the Further Reading section, there's some information about branching.

Once you've typed the "git push" command, git will ask you for a username - this is the username you signed up with github under. Then, it will ask for a password. When you type, you may be used to seeing asterisks(*) appear, but nothing will show up instead of just displaying your password for the world to see - so don't worry about typing it in in front of your partner.

After this, head over to your Github profile. You should see your new repo has been created, and any files you've added should have been pushed to the server. This is the simplest way to back up your work to the cloud, share code between teams, and make sure you remember what you did, when you did it, with notes to yourself.

Now repeat this for your partner so both of you have the code for the exercise saved in your github accounts.

If you're comfortable with that, try going back and adding the remotes to Exercise 01.


Further Reading
========

http://try.github.com

Information about Branching  
http://pcottle.github.com/learnGitBranching/  

Here's a very through overview of Git and how it works.  
http://ftp.newartisans.com/pub/git.from.bottom.up.pdf  

Even more through, is this book:  
http://git-scm.com/book/en  

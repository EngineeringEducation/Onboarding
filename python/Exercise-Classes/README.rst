====================
Exercise for Classes
====================

Ubermelon sells different types of melons. The ways our melon prices and
availability vary can be:

- The species (e.g., Watermelon versus Cantaloupe)

- Whether this melon is imported or grown domestically.

- The shape of this melon. Most melons are natural-shaped (often round or
  bullet-shaped) but we also sells melons which have been grown to be square,
  at a considerably higher price.

- The season of the melons.

Up until this point, we've kept data about the melons in a simple Python
file (``data.py``) which is a list of tuples of this information.

Our salespeople use the following rules to determine the price of melons:

- Normally, melons cost $5

- The base cost of Casabas and Ogens is $1/each more, though, as they're
  harder to grow.

- Imported melons cost 1.5 times as much as they otherwise would, because of
  shipping cost.

- Square melons cost 2 times as much as they otherwise would, because of the
  much more intense effort to grow them.

Right now, we've just had our salespeople look at the data file and figure out
how much a melon will cost by applying all of these rules to the melon.

So, for example, an foreign-grown natural-shaped Christmas melon would
cost $5 * 1.5 (for being foreign-grown) = $7.50. A Casaba is $9 (base price $5
plus $1 for being a Casba or Ogen, times 1.5 for being imported).

We have some new challenges, though: some of our melons are
discounted for multiple purchases. Starting now, we're offering the following
discounts:

- If you buy 3 or more Watermelons, you get all of them at 75% of what the
  cost would otherwise be. So, determine the price for all of the Watermelons
  someone wants and, if it's three melons or more, multiply that total by
  0.75.

- If you buy 5 or more Cantaloupes, you get them all at half price (because,
  really, who likes Cantaloupe *that much*?).

Part I: Classes
===============

This is really a pain for our salespeople, and also makes it hard to get
data right for our web site.

As we've been learning about classes, this seems like a great time to use
classes--since we're combining data *and* functionality.

Look at our requirements:

- Define a class for each melon type that we sell. You should do this in
  the ``melons.py`` file (which is empty at the beginning except for
  a docstring).

- Add attributes for things like their name/color/shape/origin/seasons

- Add a method with the following signature::

    def get_price(qty):
        """Determine price for this quantity of melons of this type.

        Return a float of the total price.
        """

  This way, we can ask each melon class how much `x` number melons of that
  type should cost.

  Write the functionality to determine the price for each class of melon.
  This will be different for our different types of melons, so this function
  will be different, slightly, for each class you made.

- You can test your code by going into the python console and interactively
  playing with your classes.

  To do so::

    $ python -i melons.py

  The "-i" command for Python means "run in the interpreter"--it runs your
  Python module (file) and leaves you in the Python interpreter, so you can
  test out your code.

  **Bonus idea:** try it as ``bpython -i``. Yay, code completion, docstrings,
  and pretty colors!

  At this point, you should be able to try things like::

      >>> w = Watermelon()
      >>> w.get_price(2)
      10
      >>> w.get_price(3)
      11.25

  (the latter price because of our special rule about discounts for quantity
  purchases of Watermelons)

When you've built these classes, please **stop and ask for a code review**.


Part II: Hierarchies
====================

Our CEO is always toying with changing the base price of melons from $5 to
something else, sometimes on a whimsical basis.

Right now, you probably have code that looks like this::

    class Watermelon(object):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = 5.0 * qty
            if qty >= 3:
                total = total * 0.75
            return total

(and similar classes for all of the other melons)

It would be a pain to change the base $5.00 cost of melons for each of the
melons by changing each class individually, though.

You *could* make the base price come from a constant, like::

    BASE_MELON_PRICE = 5.00

    class Watermelon(object):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = BASE_MELON_PRICE * qty
            if qty >= 3:
                total = total * 0.75
            return total


That would make it easier to update--but it wouldn't be flexible enough for
our CEO. Sometimes the CEO talks about making the base price vary on dynamic
things, like the weather that day or the day of the week, or other things.
If we had to put that dynamic logic into each melon type class, we'd be
duplicating a lot of code--so even though it's $5 for now, we want to
plan ahead.

We could solve this by making all of our melons subclass a common base class
(`Melon` might be a good name for this!), and they could get the base price
of melons by calling a method, `get_base_price()` on the parent `Melon` class.
For now, this ``get_base_price`` could just return 5--but we're creating a
"hook" where we could later do something smarter/more complex.

That is, if you change the base price on the Melon class, all of your other
classes would still be able to get the newly-updated cost.

When you've done this, please **stop and ask for a code review**.


Part III: Abstract Classes
==========================

So, in the last part, you probably ended up with a parent class like::

    class Melon(object):
        def get_base_price(self):
            return 5.00

and child classes like::

    class Watermelon(Melon):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = self.get_base_price() * qty
            if qty >= 3:
                total = total * 0.75
            return total

That's great.

However, some of our other programmers didn't realize we couldn't sell
"plain melons" (ie, not of any particular species!) -- they would create
instances of the `Melon` class and try to get their price::

    >>> melon = Melon()
    >>> melon.get_price(5)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: Melon instance has no attribute 'get_price'

How can we suggest to other programmers that they shouldn't ever directly
create instances of the base `Melon` class?

There's a good naming convention for this. Go ahead and rename this class
and fix the code to use this naming convention (hint: read about how to do this kind of
replace-everywhere for Sublime! Good programmers are lazy).

However, even with this name change, some of our programmers STILL are
trying to instantiate from this class (that is, make instances of this class).

Think about a way you could prevent them from doing so.

You could do this either by:

- allowing them to make an instance of this class, but giving a better
  error message when they try to call ``get_price(qty)`` on it (so you could
  raise a message when ``get_price(qty)`` is called on the base class
  directly).

or

- disallowing them from making an instance of this class at all. Is there
  a method that is always called when an object is created? Can you raise
  an error on the base class if you tried to make an instance directly from
  it?

Which of these options do you like better?

Whichever you choose, learn how to "raise" an error ("exception") in Python.
You may find https://docs.python.org/2/library/exceptions.html helpful here.
Which of these errors sounds like it would be the most helpful/descriptive
to use?

When you've done this, please **stop and ask for a code review**.

BTW, notice how the Python exceptions are a hierarchy of classes--
this let's you catch a general class of error or a very specific error,
depending on which is what you want. So you can say things like::

    try:
        7 / 0
    except ZeroDivisonError:
        print "You can't divide by zero!"

or::

    try:
        7 / 0
    except ArithmeticError:
        print "You made some sort of mathy error"

Depending on whether you want to handle zero-division distinctly or just like
other math errors. You could even write something like::

    try:
        7 / 0
    except ZeroDivisonError:
        print "You can't divide by zero!"
    except ArithmeticError:
        print "You made some sort of mathy error"

Which would handle all cases, but handle zero-division separately.

Pretty neat, huh?

Part IV: Flexing Our Hierarchies
================================

Right now, you probably have code like::

    class Watermelon(AbstractMelon):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = self.get_base_price() * qty
            if qty >= 3:
                total = total * 0.75
            return total

That's fine, but we have a few things we can improve.

Watermelons are our standard base price (except for quantity discounts)
since they're natural-shaped and domestically-grown. If our supplier for
Watermelons switched to being foreign-grown, we'd have to do two things:

- change that attribute to ``imported = True``

- update our ``get_price(qty)`` method to multiply the final price by 1.5,
  since that's our markup for imported watermelons

It's easy to imagine that we'd do the first and forget to do the second.
Plus, even if we did, we'd be sprinkling the logic for this all over
the place.

For example, we could do this::

    class Watermelon(AbstractMelon):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = self.get_base_price() * qty

            if qty >= 3:
                total = total * 0.75

            if self.imported:
                total = total * 1.5

            return total

And then we can't forget to update the price if the origin changes--but
we'd have a lot of duplicate code throughout.

Better would be for our base class, ``AbstractMelon``, to handle much of
our price calculating, but for it to rely on the attributes set on the
individual melon type.

In this ``get_price()`` for `AbstractMelon`, We'd need to get the "add-on" $1
for Casaba and Ogen somehow, then the total based on shape/origin/quantity.
For Watermelons and Cantaloupe, we'll need to then apply our discounts.

Create a method on the base class to handle this work. Where needed,
use that method from the individual melon classes.

To do this, it's probably going to be helpful to put an attribute on the
the Casaba and Ogen class to keep track of their $1 base price bump;
your logic in the base class ``get_price()`` could use that.

When you've done this, please **stop and ask for a code review**.

Part IV: Is the Melon Available?
================================

*(This section is advanced and optional)*

For availability, we keep track of the season that a melon is available for
purchase. We define these as:

- Winter: Jan, Feb, Mar
- Spring: Apr, May, Jun
- Summer: Jul, Aug, Sep
- Fall: Oct, Nov, Dec

Add a function onto our AbstractMelon class that tells us whether a
particular melon is available for sale today.

To do this, you'll want to learn about the Python `datetime` library. This
has features to give you today's date, as well as ways to figure out the
month part of that.

Create a function that returns `True` or `False` to let us know whether
this melon is available today.

Advanced: Update this function to *optionally* take a date argument so
that, if one is given, we check for melon availability on that date. If
no argument is given, it should use today's date. This requires a little
clever thinking around optional arguments.

When you've done this, please **stop and ask for a code review**.

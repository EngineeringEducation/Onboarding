===========================
Rubric for Classes Exercise
===========================

Here are the expectations/suggestions for TAing the Classes Exercise.

Part I
======

In this part, we want them to show that they can build standard classes.

A good outcome would be a series of standalone classes, like::

    class Watermelon(object):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = 5.0 * qty
            if qty >= 5:
                total = total * 0.75
            return total

    class Ogen(object):
        species = "Ogen"
        color = "tan"
        imported = False
        shape = 'natural'
        seasons = ['Spring', 'Summer']

        def get_price(self, qty):
            total = 6.0 * qty
            return total

    # rest of classes follow

Things to look for:

- Did they subclass ``object``?

- **naming conventions**: are the class names in CamelCase?

- Did they add the attributes for each melon type? Did they think to add
  a "name" attribute? (If, point out how it might be hard to print the
  name of the melon, especially for melons like 'Santa Claus', where the
  name would look ugly if it was printed SantaClaus)

- Did they remember to make Casaba and Ogen melons be $6 each?

- Did they make the foreign melons cost 1.5 as much?

- Did they make the square melons cost 2.0 as much?

- Did they put in the quantity discounts for Watermelon (75% for 5+) and
  for Cantaloupe (50% for 3+)?


Part II
=======

The goal here is for them to end up with a `Melon` parent class with a
``get_base_price`` method, like this::

    class Melon(object):
        def get_base_price(self):
            return 5.0

And then have the melon type classes use that::

    class Watermelon(Melon):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = self.get_base_price() * qty
            if qty >= 5:
                total = total * 0.75
            return total

    class Ogen(Melon):
        species = "Ogen"
        color = "tan"
        imported = False
        shape = 'natural'
        seasons = ['Spring', 'Summer']

        def get_price(self, qty):
            total = (self.get_base_price() + 1) * qty
            return total

Some things to look for:

- Did they remember to have the melon type classes subclass Melon?

- Did they remember to add $1 to the base cost for Ogen and Casaba?


Part III
========

The goal here is for them to understand that the Melon class is an
"abstract class" -- it shouldn't be instantiated directly. They also will
be learning about raising exceptions.

This is often done with one or both of these methods:

1. Name it something obvious ("BaseMelon" or "AbstractMelon")

2. Prevent instantiation

A good outcome could be::

    class AbstractMelon(object):
        """Common logic for all melons.

        Not meant to be instantiated directly.
        """

        def __init__(self):
            raise NotImplementedError("Don't make instances of me")

        def get_base_price(self):
            return 5.0

Alternatively, they could not block instantiation directly, but give an
error on calling ``get_price()``::

    class AbstractMelon(object):
        """Common logic for all melons.

        Not meant to be instantiated directly.
        """

        def get_base_price(self):
            return 5.0

        def get_price(self):
            raise NotImplementedError("Can't use this directly")

The first is a better outcome, though--it prevents trying to make instances
immediately, so you get an error earlier and a more obvious place.

We also wanted them to discover NotImplementedError. They could raise this
either like this::

    raise NotImplementedError

or like this::

    raise NotImplementedError("providing a string explanation here")

The second is nice to learn, as it lets them provide some documentation for
their error.

Part IV
=======

The goal here is to move some of the common logic to the parent class, while
getting data from the subclass.

A good outcome would be::

    class AbstractMelon(object):
        add_on = 0

        def __init__(self):
            raise NotImplementedError("Don't make instances of me")

        def get_base_price(self):
            return 5.0

        def get_price(self, qty):
            each = self.get_base_price() + self.add_on
            total = each * qty

            if self.imported:
                total = total * 1.5

            if self.shape == 'square':
                total = total * 2

            return total

    class Watermelon(AbstractMelon):
        species = "Watermelon"
        color = "green"
        imported = False
        shape = 'natural'
        seasons = ['Fall', 'Summer']

        def get_price(self, qty):
            total = super(Watermelon, self).get_price(qty))
            if qty >= 5:
                total = total * 0.75
            return total


    class Ogen(AbstractMelon):
        species = "Ogen"
        color = "tan"
        imported = False
        shape = 'natural'
        seasons = ['Spring', 'Summer']

        add_on = 1

This may be hard for them to get through and may need hints, especially around
the ``add_on`` attribute.

Some things to look for:

- There's no need for them to define ``add_on`` on the melons that don't have
  an add-on cost; they can put this on the `AbstractMelon` and inherit this
  common class.

- All of the logic of multiple-by-qty, adjust-for-origin, adjust-for-shape
  should be in the parent ``get_price()``

- Are they calling ``super()`` properly?

- There's no benefit (and it would be bad design) to put a superfluous
  ``get_price()`` on the melons that don't need it (everything but
  Casaba and Ogen); these melons should just inherit and use the
  ``get_price()`` method.

Part IV
=======

This part is optional and is really here to just give advanced pairs something
to work on if they finish early.

They'll need to get today's date and then check to see if we sell that
melon today::

    class AbstractMelon(object):
        # ... rest of class stays same
        def available_now(self):
            today = date.today()
            month = today.month

            if month == 1 and 'Winter' in self.seasons:
                return True
            if month == 2 and 'Winter' in self.seasons:
                return True
            if month == 3 and 'Winter' in self.seasons:
                return True
            if month == 4 and 'Spring' in self.seasons:
                return True
            if month == 5 and 'Spring' in self.seasons:
                return True
            if month == 6 and 'Spring' in self.seasons:
                return True
            if month == 7 and 'Summer' in self.seasons:
                return True
            if month == 8 and 'Summer' in self.seasons:
                return True
            if month == 9 and 'Summer' in self.seasons:
                return True
            if month == 10 and 'Fall' in self.seasons:
                return True
            if month == 11 and 'Fall' in self.seasons:
                return True
            if month == 12 and 'Fall' in self.seasons:
                return True

            return False

(They could also handle that logic differently; the core parts are for them
to get the month and check the list of seasons.)

For the advanced-advanced part, they'd need to default to today's date.
They might try something like::

    def available_now(self, the_date=date.today()):
        month = the_date.month
        # ... rest of code here

But, of course, Python doesn't allow dynamic function/method arguments (if it
did, that would be when the program started, which might be months from today
if this were a long-running web server!)

Instead, they'll need to discover the idea of a "marker" argument. This might
require some cleverness and Googling and is pretty advanced::

    def available_now(self, the_date=None):
        if the_date is None:
            the_date = date.today()

        month = the_date.month
        # ... rest of code here


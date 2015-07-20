# Backbone.js - JS MVC and YOU!

### Related Tutorials:
* [JS Is Sexy Backbone Megatutorial](http://javascriptissexy.com/learn-backbone-js-completely/) (★★★★☆) (30 Hours)
* [http://codebeerstartups.com/2012/12/a-complete-guide-for-learning-backbone-js/](codebeerstartups Megatutorial) (★★★★★) (5-10 hours)

### Docs
* [Backbone](http://backbonejs.org/)
* [Underscore](http://underscorejs.org/)


### JS Prereqs

* [JS Objects](http://javascriptissexy.com/javascript-objects-in-detail/)  
* [Scope](http://javascriptissexy.com/javascript-variable-scope-and-hoisting-explained/)  
* [Closures](http://javascriptissexy.com/understand-javascript-closures-with-ease/)  

### Assignment Prereqs
* [Too Much Not Enough](too_much_not_enough.md)

Now, read through these (just reading at first):  
* [Models](http://backbonetutorials.com/what-is-a-model/)
* [Views](http://backbonetutorials.com/what-is-a-view/)
* [Collections](http://backbonetutorials.com/what-is-a-)collection/
* [Routers](http://backbonetutorials.com/what-is-a-router/)

These basic parts of backbone.js are what we'll be using to assemble an app.  

### Assignment

Head back to [Too Much Not Enough](too_much_not_enough.md), which you should have completed by now. If not, you should be able to get it together quickly.

Having an already completed psudeo-view is a pretty common time to add a javascript MVC framework. We have an idea of what data we want to display, and we have an idea of what kinds of interactions might be possible from our view. With a standard grid-based layout, everything tends to turn into repeated chunks of code with only the data changed, and so we can look at these and get an idea of our data models.

Take a moment and do these things:
* Look for repeated code and write down models you think would come out of that code
* Take note of sub-models that are "implied" by some of the controls and data on the page.
* Write down the names and obvious attributes of each data model

Once you've written down your models and their attributes, head back over to the [Models](http://backbonetutorials.com/what-is-a-model/) example, and put some in a script tag embedded on the "search" page. 

We'll factor out (organize) this code later by putting each model in it's own file, but when we're working on them it helps to put them where you can see them all at once. 

Now that you have models on your page, let's create views for them. You'll want to use templates, [this giant megatutorial](http://codebeerstartups.com/2012/12/how-to-use-templates-in-backbone-js-learning-backbone-js/) has a good section on them. 
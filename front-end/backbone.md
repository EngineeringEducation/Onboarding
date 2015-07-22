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
* [Collections](http://backbonetutorials.com/what-is-a-collection/)
* [Routers](http://backbonetutorials.com/what-is-a-router/)

These basic parts of backbone.js are what we'll be using to assemble an app.  

## Exercise


#### Start
Head back to [Too Much Not Enough](too_much_not_enough.md), which you should have completed by now. If not, you should be able to get it together quickly.

Having an already completed psudeo-view is a pretty common time to add a javascript MVC framework. We have an idea of what data we want to display, and we have an idea of what kinds of interactions might be possible from our view. With a standard grid-based layout, everything tends to turn into repeated chunks of code with only the data changed, and so we can look at these and get an idea of our data models.

#### Planning
Take a moment and do these things:
* Look for repeated code and write down models you think would come out of that code
* Take note of sub-models that are "implied" by some of the controls and data on the page.
* Write down the names and obvious attributes of each data model
* Write down the actions users can take on each page- can they create? update? delete? Do they cause interactions between models? Are they finding / sorting / filtering models? Don't forget that User is also a model.

It's important to recognize what kinds of interactions fall under what category. Liking a post on facebook could mean you're creating a like, or it could mean that you're updating a post. Either way though, it is an interaction between a User model, and a Post model, and potentially a Like model. It's up to you to decide how to store those interactions.


#### Create Models
Once you've written down your models and their attributes, head back over to the [Models](http://backbonetutorials.com/what-is-a-model/) example, and put some in a script tag embedded on the "search" page.

An example:  
```javascript
var Fruit = Backbone.Model.extend({
	idAttribute: "_id",
	defaults: {
		name: "Unnamed Fruit",
		img: "http://placehold.it/350x150"
	}
});

var Fruits = Backbone.Collection.extend({
	url: "/fruit",
	model: Fruit
});
```
**This assumes we have a URL that we're sending fruit to and getting it from. Unless you have a server setup for this, don't add a URL.** Also, "fruit" is probably a bad model name, as we're not only storing fruit. Come up with a model name that accurately describes all the different types of fruits, veggies, berries, and other growing things.

We'll factor out (organize) this code later by putting each model in it's own file, but when we're working on them it helps to put them where you can see them all at once.

#### Test your models
Test out that you can create models by inputting data for them. Backbone models will fill in their attributes if you pass them an object literal, so take a few of the examples from your page and test models like so:
```javascript
var apple = new Fruit({
	name: "Apple",
	img: "http://cdn-www.i-am-bored.com/media/thumbnails/apple_for-diabetics[1].jpg"
});

var fruits = new Fruits([apple, pear, watermelon])
```
Be sure to understand each line of the above example and then translate it to your own code, instead of just copy-pasting. Ensure that you can create models, add them to collections, and view their properties by logging `apple.attributes` to the console.


#### Views
Once you have models on your page, let's create views for them. You'll want to use templates, [this giant megatutorial](http://codebeerstartups.com/2012/12/how-to-use-templates-in-backbone-js-learning-backbone-js/) has a good section on them. 

#### Using Templates for Views
Take the repeated HTML code from your page that you used to intuit the models and put it in `<script type="text/template" class="template hide">` tags for each small block that is repeated. Use the templating language of your choice to embed variables.  
An example would be:   
```html
<script type="text/template" class="template hide" id="fruit_template">
	<div class="col-md-3">
		<div class="image"><img src="{img.src}}"></div></div>
		<div class="title">{{title}}</div>
	</div>
</script>
```

** This is an example, using an imaginary templating language. Don't just copy-paste this and expect it to work, do some research on what template language you want to use first. **


#### Rendering Views
Now, in your view, you'll want to put rendering code. Backbone doesn't have hidden magical methods to take a template and render it and then append it to the DOM. We really just have to write the javascript code to find the template and get the contents from it (`$("#fruit_template").text()`), then create a function that can take an object (like `apple.attributes`) and use it's keys to fill in the variables in a template (`this.template(this.model.attributes)` in the code below.)
An example:  
```javascript
var FruitView = Backbone.View.extend({
	tagname: 'div',
	attributes : {
		"class" : "col-md-3"
	},
	template: _.template($("#fruit_template").text()),
	render: function() {
		this.$el.html(this.template(this.model.attributes));
    	return this;
	}
});
```

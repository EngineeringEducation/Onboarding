Sorting Hat
===========

[The Sorting Hat](http://www.youtube.com/watch?v=hbjksQapIfg) in Harry Potter is magically able to place students in their correct houses.  In this exercise, we're going to build our own version of the sorting hat, but instead of using magic we'll be using the power of Javascript.  Which is sometimes like magic.

###Dramatis Persone###
[**The DOM**](https://developer.mozilla.org/en-US/docs/Web/API/document) - Document Object Model  
[`document.getElementById()`](https://developer.mozilla.org/en-US/docs/Web/API/document.getElementById) - a method for finding things by their IDs  
[`element.addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget.addEventListener) - a method for responding to events  
**variables** - Various containers for information  

###Table of Concepts###
- Starting out with a template  
- Seperating the idea of a form from having to submit to a webserver  
- Interacting with the DOM  
- Event Listeners  
- Modifying the DOM with JavaScript (in response to an event)  


###Step 0 - In which we set up our Template ###
Open up [sorting_hat.html](https://github.com/hackbrightacademy/Javascript2/blob/master/sorting_hat.html). It's got a basic bootstrap template there for you, so you don't have to look at those ugly default-internet fonts. It doesn't have much else though, so we'll need to add some things.


###Step 1 - In which information is gathered, and a counter is initialized###
First, let's take inventory of the things we need:  
- We need to know how many people we'll be sorting, so we can sort them evenly  
- We need the names of the students who are being sorted  
- We need places to put them after having been sorted  

Let's start with just the first one, and then you can do the rest yourself.  
Since we need to gather some information, let's put a form on the page. **_Since this form doesn't have to submit anywhere, we don't want an actual `form` tag_**. If we *did* add a form tag, it would submit the page to itself, instead of activating our cool JS event. We don't want that.  
  
Add a new `div` somewhere inside the container `div`, give it the `class` of `form`. 

Inside that new `div`, put an `input` tag, another (empty) `div` called "count", and a `button`. Give them all IDs.

```html
	<div class="form">
		<input type="number" id="student_count">  
		<button id="set_student_count">Set Student Count</button>  
		<div id="count"></div>
	</div>
```
The empty div is where we'll be placing a count of the number of students we have sorted so far.  It's content will get filled in by our Javascript code when we place a student.  By placing it in the HMTL now, we've handled the layout and position of counter and we can let our Javascript code focus on the content.

Next, we're going to practice button-clicking actions that modify the page.

###Step 2 - In which Javascript is written, and placed in our page ###
To start, we're going to create a `<script>` tag where we can place our Javascript code.  At the bottom of the page (at the end of the `body` tag) is a good place: 
```html
	<script type="text/javascript">
		//Javascript goes here, and runs when the page loads.
	</script>
```

Next, we need a place to store the information we get from the user. Create a globally scoped variable like this, outside of any functions.
```javascript
	var studentCount = 0;
```
###Step 3 - A button is identified, clicking noises are heard ###

To do that, we'll need to make something that responds to a button click, but for that we'll need to **find the button in the DOM**. Good thing we gave it an ID. IDs are supposed to be unique, so we can target single DOM nodes with them.
```javascript
	var button = document.getElementById("set_student_count");
```
And now we can spy on our button, by adding event listeners to it. This is similar to a wiretap, only we don't need a warrant to do it. (Ok so it's exactly like a wiretap these days apparently.)  
Basically it looks like this:  
```javascript
	button.addEventListener(event, function);
```
The **first argument** is a string name of an event we want to listen to. It should be "click" (with the quotes).  
The **second argument** is a function. We can pass it any function by value, or we can write *idomatic javascript* by declaring a function right then and there.  

Here's a function being declared in place:
  
```javascript
	button.addEventListener('click', function(){});
```

###Step 4 - Events, having transpired, change the nature of the page###
  
Open that function up by dropping a few line breaks within it. Inside that function, let's tell it what to do whenever that button gets clicked.  

Add a line of code underneath each comment:  
```javascript
	button.addEventListener('click', function(){
		// Create a variable that will store the div object where we will display 
		//  the student count by using document.getElementById("count")

		// Create a variable to store what the user entered into the text input field.
		//    You can use document.getElementbyId("student_count").value
		//    If the field is empty (or not a number), set it to 0.

		// Add the user entered value to studentCount (the global variable we set
		//    up earlier in Step 2).

		// Display the new value of studentCount in the div object (the "count" 
		//    div) we saved ealier.  Use the .innerHTML property to update the
		//    contents of the div

		// Reset the input field (student_count) changing the .value attribute to 0

	});
```
Great! Now we've used a button click to get data out of a form and change the page, without having to use a server at all!

We're going to do that again, but this time we're going to be collecting student names, and sorting them.

We need to add another input field and button, but this time the type will be `text`, and the button will say "Sort!"

Instructions:  
- Take the value from the student name input field  
- Pick a house at random (probably keep these in some array or... object?)  
- Check to see if the house is "full". Full means that the house has less than the number of students we're sorting divided by the number of houses. Yes, that does mean you'll need to keep track of who is in each house. (Protip: `document.getElementsByClassName()` will help you here )
- If the house is full, make sure you pick a new house, and do the same checks.  
- Put the student into the house you picked, by displaying the student's name inside the house  
- Decrement the count of students from the count div.  
 
Bonus:  
- Show the sorting hat, as well as the student's name, al la: "Stella LeFevre: Gryffindor!!"  
- Turn house names green as they get full  
- Display a random quote from the sorting hat that goes with the house's saying (or make up hilarious new ones)  
- Once you've sorted all the students, display an image and get rid of (hide) the student input field.  
- If we add more students to be sorted, put the input field back.  
Laundry Timer
=============

Almost no one has private laundry in SF. Fortunately, most people have a laundromat near enough to their house, and so they leave their laundry there. I usually do multiple loads at once, so I've developed a queueing system to handle it.  

This is a much more complicated exercise than the previous one. We'll be reintroducing the concept of a **main event loop** ([remember this?](https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise01#introduction)). Rather than waiting for user input however, the main event loop will just run every second. Our functions are going to be executed either in response to **events** (mouse clicks), or once a second.

###Dramatis Persone###
[`document.getElementsByClassName()`](https://developer.mozilla.org/en-US/docs/Web/API/document.getElementsByClassName)  
[`element.className`](https://developer.mozilla.org/en-US/docs/Web/API/Element.className)  
[`document.createElement()`](https://developer.mozilla.org/en-US/docs/Web/API/document.createElement)  
[`window.setInterval()`](https://developer.mozilla.org/en-US/docs/Web/API/Window.setInterval)
  

###Table of Concepts###
Event Loops  
Timers / Intervals  
Event Listeners  
DOM Node Creation  
DOM Tree Manipulation [(The `document` Object)](https://developer.mozilla.org/en-US/docs/Web/API/document)  
DOM Node Manipulation  [(The `element` Object)](https://developer.mozilla.org/en-US/docs/Web/API/element)  




Sometimes, when someone in the real world wants some software written, you get a set of requirements. Basically it's just a list of behaviors people want, with a little bit of information about what buttons they're interested in seeing. Sometimes you won't have all the information you need in the requirements, which might require a little bit of freestylin'. Sometimes you'll want to go back and demand more information however, especially when you're a junior developer.  
### Requirements:###

- We want to be able to start a timer
	- The timer's length should be specified by an input box
	- We should have an input box for washer length, and dryer length
	- We should have a button that creates a new load of the specified type
- We want to be able to have multiple timers going
- We want to be able to watch the countdown of each timer update
- Once a timer is done, we want to indicate that it's finished somehow


### Let's get some information ###

Start by opening [laundry.html](https://github.com/hackbrightacademy/Javascript2/blob/master/laundry.html)
We're going to modify it so we can get some information from the user, and interact with it to make our timers run.

We need to get this information initially:
- How long does a washer load take?
- How long does a dryer load take?

Create a form that gathers that information using number-type input fields. Also, add two buttons to the form, one that says "New Washer Load" and one that says "New Dryer Load". This is the same kind of "not submitting" form we used in the last exercise, so don't use a `form` tag. Just use a `div`.  
  
Once you've got a form somewhere on the page we need to create 4 functions.  
  
### The Main Event Loop ###
We'll be running these functions once every second - create functions with names, so we can refer to them later.  

The first function needs to be able to find all of the times on the page, and decrement them. Probably call it `decrementCounters()`.    
- We'll want to use `document.getElementsByClassName()`. It provides an array of DOM nodes.  
- Loop through the DOM nodes, and get the time from their `.innerHTML` property.   
- Decrement the time by 1 second.  
- Make sure to decrement a minuite if the seconds are at 00.  

Once that works, you'll be able to call it over and over again. Open the console in your browser, call the function a few times and make sure all the counters go down by 1 second. Make sure to test that once you get to 00 seconds, the minuites decrement.

It's very important you don't try to do anything else in this function - since it will run once a second, we only want it to do **one thing** so we can predict it's behavior.

The second function needs to be able to stop a timer once it reaches "00:00". We'll want to run it once a second too, but we want it to run after the decrementer function runs.
- Find all the timers again. See if any of them are at "00:00".  
- If so, remove the timer class.   
	- You can do this by setting the `.className` property of the element.
	- You may want to do something else here to alert the user that their timer has ended.  


Once you've tested that these functions work by calling them in the Javascript Console within Chrome Developer Tools a few times, it's time to set up our main event loop.

```javascript
setInterval(function(){
	decrementCounters();
	stopEndedCounters();
},1000)
```

This code runs once a second - it calls our decrementer, and then it calls our check to stop ended counters. Put it in your script tag at the bottom, then test it, and see if you can get a counter to count down to 00:00.


### The Event Listeners ###

The third function needs to be able to create a new washing machine row. 
- Find the table in the DOM
- Use `document.createElement('tr')` to create a table row  
	- This **returns** an element, so put it in a variable.  
- Use `document.createElement('td')` to create a table column  
- Set the `.innerHTML` property to be the value from the input tag from before.  
- Use `variableContainingElement.appendChild(otherElement)` to put the `td`s inside the `tr`. 
- Then, use the same method to append the TR to the table.

The fourth function needs to be able to create a new dryer row.
- Replicate the functionality from the washer row, but change the type / time.


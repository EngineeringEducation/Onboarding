# Mailing lists are harder than you think

So we’re building a mailing list. This document should help you:

* Know what you need to know

* Make a plan

* Know what to do when you get stuck

## What is this project?

We’re going to be building a site that functions like many startups you've seen before. It will have mailing list functionality, and drip email functionality.

**Main Requirements:**

* Collect users’ email addresses and a timestamp

* Saves users' email addresses in a database

* Sends an email to users when they sign up

* Sends an email to users a day after they sign up

* Sends an email to users a week after they sign up

**Stretch goals:**

* Admin user can log in with google

* View all email addresses

* Compose a message

* Save that message to disk for further use

* Send a message to all users right now

* Send a message to all users some amount of time after they sign up

* View the schedule of emails

Seems simple, right?

Node.js and the things you can make with it should empower you to build the web that exists between all of the connected devices you use every day. Node.js shouldn’t just be thought of as something for building webservers. It’s to connect programs together, be that over the network, or locally on your computer. It’s Javascript, with an interface to the full power of your operating system. That means it can read files, do computation, and connect with other resources across the internet. 

**What we’ll need to know how to do to successfully complete this project:**

* How to listen for connections coming in over the net

* How to figure out what those connections are asking for

* How to get data from those connections

* How to send that data to another program (a database)

* How to get that data back out of another program

* How to read files from the hard drive

* How to interact with an API, to send mail

* How to use another service to asyncronously perform tasks from a queue

* How to authenticate users

* How to use cookies to keep users authenticated

* How to use oAuth to get someone's user data from another service

That’s a lot! By now, you know how to approach giant problems like this: **step by step, after you have a plan**.

## General Resources:

Keep open the Express API documentation and the Node.js documentation.

Another great resource is Eloquent Javascript's Express.js tutorial and this API tutorial

## Step 0: The Simplest Possible Thing

First, let’s just create a webserver that returns Hello World! Let’s go through some of the basic "app hygiene" practices that will help us keep organized.

Open terminal, and create yourself a folder for this project with mkdir. **Stay out of finder.app for this entire exercise**, and out of it forever if you can help it. Real programmers don’t use finder.app.

Next, within that folder, git init

Now, npm init

npm will ask you several questions, press enter if you don’t know what to fill in. You can always come back later and look at your package.json file and change things. Make sure to give it a **name** (mailingList or whatever strikes your fancy); **accept the default entry point **(which is index.js), and add an author and description if you feel like it. 

Now then, we’ll be using an npm package called ‘Express’, which helps us manage a lot of common web tasks and also helps us organize our program. We need to install it however, so let’s do that now with npm install express --save

The --save switch writes that we need that package in our package.json file, so that anyone who wants to run our code only has to type npm install and it will pull down all of our packages.

Now, create index.js by typing touch index.js in your terminal. This creates a blank file. Now open up sublime text (try subl .) and add your folder to your project using the project menu.

**Time to finally write some code!**

Let’s go over the plan: 

* Create a webserver

* That responds to GET requests

* With "Hello World"

Open up your file, and require the express.js module, using var express = require("express");

[Now create a new instance of an express server](http://expressjs.com/api.html#express), by typing var app = express();

This will return you an app that’s capable of doing a lot of stuff! For now, we just want it to return hello world, so let’s look at how we can accomplish that.

[app.get](http://expressjs.com/api.html#res.get) is a handy method for listening to get requests. It listens for any requests that come in, whose path matches that of the first argument. Then, it runs the callback function supplied as the second argument. Way easier than raw node.js!

app.get("/" function(request, response) {

// We get access here to the request, so we can find out more information about what the requester wants.

// We also get access to the response object, which is the object that allows us to send a string (or other things) back to the requester.

[response.send](http://expressjs.com/api.html#res.send)("<h1>Hello World!</h1>");

 });

Now, our app will accomplish what we want, but we need to actually "hook it up" to incoming requests. The way we do this is by asking it to listen to a specific port.

Often, we don’t know the port we’re going to be listening to in advance, because it’s set by something external. In the [12-factor-app model](http://12factor.net/), we want to [store that kind of information in the environment](http://12factor.net/config), not hard-coded in our application, since that information will change from server to server, but we don’t want to have to update our code to make it run somewhere else.

So, let’s get that port from the environment by using var port = process.env["PORT"];

And then let’s listen to whatever port that may be by using app.listen(port);

Done! Now let’s run it, and set that environment variable in the same line. Use:

PORT=3000 node index.js

… in your terminal.

Check it out at localhost:3000

## Step 1: Serve HTML

Alright, so now that we can get words on a webpage, let’s start by serving some HTML! 

Obviously, writing a bunch of inline HTML in response.send() would just suck and be completely unsustainable. So let’s start by serving files.

**The plan:**

* With our existing server

* Serve HTML files from a directory

* Based on the path of the request

Make a new directory (with mkdir in your terminal!) and call it views. Now, cd into that folder and touch index.html. You should see this pop up in sublime text but if not, refresh folders from the project menu.

Let’s put some text into this file, it doesn’t matter what right now, so just throw some [lorem ipsum](http://slipsum.com/) in there. 

Express has some [very simple middleware functions](http://expressjs.com/guide/using-middleware.html), one of which lets us just use static files.

Include this line app.use(express.static(__dirname + '/views'));

This just tells express to look in the request for the path, and then look for a file that matches the path being requested. 

Try running your app again PORT=3000 node index.js and then visit localhost:3000 in your browser. You should see the contents of your file!

Notice that we didn’t specify a path, yet it rendered index.html. Webservers since the beginning of time have looked at index.html if no path was specified, and we like to stick to convention, so that’s what happens. 

Try visiting localhost:3000/index.html

Now hit localhost:3000/whatever.html

Notice it returns a nicely formatted error (instead of crashing) that says Cannot GET /whatever.html. 

Create a file called whatever.html, throw something in it. Hit the server again at that same address, and notice your file is now being served! 

## Step 2: Serve Other Files

Now, these files are just the ugliest things we’ve ever seen. We don’t typically just serve plain-jane HTML with no CSS, but we don’t want to clutter up our views directory with a bunch of CSS and JS files, especially since the server is made out of JS files- it would be too hard to tell what was what. Let’s create a "static" directory, for static assets. When we use the term static, we mean, we aren’t going to manipulate it with the server before we send it out. We’re doing the same thing with our HTML, but as you can probably guess, that won’t always be the case.

**The Plan:**

* Serve files that don't change from request to request from the static directory

* Install bootstrap

* Include it on the HTML we're serving

Add this line, and create the corresponding folder:

app.use(express.static(__dirname + '/static'));

Now, in your /static folder, create /images /stylesheets /javascripts. This is where you'll put the files you write that are static. Next, we'll install other libraries and packages using Bower.

## 2a: Using Bower to install dependencies

The easiest way to install things like bootstrap and jQuery is to **use bower****_. _**To use Bower, make sure it is installed by typing npm install bower -g. Next, in your project directory, create a file called .bowerrc (note that it starts with a dot). Now, in that file, add some json:

{

	"directory": "./static"

}

Which tells bower where to save the things you want to install. Much like npm is a package manager for node.js and server-side scripts, bower is a package manager for front-end packages, like bootstrap, jquery, and modernizr. 

Once you have your .bowerrc file configured and saved, go ahead and type bower install bootstrap.

You can now look in your static directory, where you’ll see Bootstrap and jQuery are now installed! 

## 2c: A Static Webserver

Alright, so now we literally have everything we need to host a static webserver. It’s not the fastest, most optimized server ever, but it is the simplest, fewest lines of code we need to get a site up and running. 

Head over to the [bootstrap template](http://getbootstrap.com/getting-started/#template), grab it, and throw it in your index.html file. Now, we need to fix the references in the file so that they point to where bootstrap actually lives on our server. 

<link href="/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet"> 

is what your CSS file needs to look like, see if you can fix the JS reference yourself.

Now it’s time to make this page useful. 

## Step 3: Forms, Reading Them

We knew going into this that we’d need to get some data. Unfortunately, we can’t just serve static files any longer, we need to be able to process information from a request, and then do something with it. For this, we’ll need to read information from a POST request, and for that, we’ll need middleware. 

Let’s install the npm package, body-parser. Don’t forget the --save switch, so that it writes it to our package.json file.

Once you’ve done that, it’s much easier to look at the request body! But, we haven’t gotten a request body to look at before, and we won’t without an HTML form. 

HTML forms are our way of telling the browser how to format data so that we can read it later. 

Put a form on your page that looks like this:

<form action="/submit" method="POST">

Enter your email address : <input name="email" type="email" />

</form>

You should now have a really basic form on your page. You should be able to enter your email address, and press [enter] to submit. You can also throw a submit button on there if you want to, I guess.

Ok, now submitting should get you something that says "Cannot POST /submit". Let’s fix that error!

First, include body-parser the same way we included the express app, var bodyParser = require('body-parser');

Now let’s configure this middleware the same way we configured our static middleware:

app.use(bodyParser.urlencoded({ extended: true }));

app.use(bodyParser.json());

This will help us parse all of that messy data that comes in as a post body as some nice json saved on the request object. This is **middleware** that’s been pre-written for us. In order to understand middleware, let’s write some ourselves!

## Step 3a: Log it out for great debugging

Put this code as the first call to app.use(), above the static middleware routing and above the request body parsing. This way, it will run before anything else, but will allow other requests to be parsed.

//logging middleware

app.use(function(req,res,next) {

	console.log("Request at ", req.path);

	next();

});

This puts in the console every path that is requested, and then it tells express to go on running anything else that would respond on that path. Run your server, and hit localhost:3000/index.html and watch the requests come in. You’ll also see all of the static requests, so you should see the calls for bootstrap’s CSS and it’s JS. Notably missing is the request for jQuery, since we didn’t actually change the jQuery link, it hits a server that isn’t ours. 

## Step 3b: Respond to the POST

Use the app.post() to see what we get in the request body on the path we’ve included in our form:

//Respond to POST requests

app.post("/submit", function(request,response,next) {

	console.log(request.body);

});

This won’t do anything other than log out what we’re getting from the request, but let’s test it. 

Head over to your browser and enter an email and hit [enter] or submit if you put yourself a fancy button in there. Then. look at your console, you should see something like:

{ email: 'liz@tradecrafted.com' }

This is an actual object, not a string, so we can actually access it via request.body.email or request.body["email"]. 

Let’s actually respond to the post with response.end- echo back the email and thank the user for trusting you with that valuable piece of data. 

## Step 3c: Some creativity

[Take a few minutes, and add some style to your page. ](http://24ways.org/2012/how-to-make-your-site-look-half-decent/)

Make it look like somebody loves it. Maybe add some of them fancy buttons, or even a background image. 

## Step 4: You Gotta Persist

Time for some serious programming action - what good is it to get these emails if we don’t save them? For this, we’re going to finally use our first database.

If you haven’t go ahead and [download postgres.app](http://postgresapp.com/). You’ll need to start the app as well, keep it in your applications folder. If you see a little elephant in the top of your bar, it’s running.

Know SQL? Great. If not, [head over to SQLZoo](http://sqlzoo.net/wiki/Main_Page) and learn you some basic CRUD operations. 

## Step 4a: The Database Itself

In a new terminal window or tab, type psql -h localhost

Now we’ve got a connection to our local postgresql server. We’re not actually going to create things in psql right now, we’re just going to do a little touring of what is there.[ A cheat sheet of psql commands is here.](http://blog.jasonmeridth.com/posts/postgresql-command-line-cheat-sheet/)

It’s common practice to have a "database setup" or "seed" file. It’s a file that contains all of the SQL commands needed to create a database and populate it with the required tables. It also is usually pretty readable, so we can use it as a reference to see what our tables look like. 

touch schema.sql and then open it in Sublime Text. 

Here we’ll put the SQL statements we need to create our database, and create all of the tables we need to run our app. 

**Creating a Database**

To create a database, run the following statement: CREATE DATABASE databasename; 

Once you do this, your connection string will look (locally) like postgres://localhost:5432/databasename

This is something you’ll want to store in your environment as DATABASE_URL, much like our PORT variable. In production, this will come from our host. 

**Creating Tables**

To create a table to save our emails in, we’ll need to use the CREATE TABLE statement. We need to store several pieces of information. 

Here’s an example from our messagehub app:

CREATE TABLE messages (

  type_token varchar(100) NOT NULL,

  channel_token varchar(100) NOT NULL,

  user_name varchar(100) NOT NULL,

  message_text text NOT NULL,

  message_timestamp timestamptz DEFAULT localtimestamp NOT NULL

);

You’ll need to create some tables that keep track of:

* Email addresses

* When emails were added

* What emails need to be sent

* What emails have been sent

Once you’ve written the create table statements, you can run the file you’ve created by typing psql databasename -f schema.sql

## Step 4b: Connecting in your app

Now that you have an actual database, it’s time to connect from your app.

Install (and make sure to save) an npm module called "pg". Once you’ve got that installed, require it in your app. Call the variable "pg", as it’s convention to call the variable the same or very similarly to the name of the module. 

Next, get your connection string out of your environment with process.env["DATABASE_URL"] (and watch out for those smart quotes.)

**A Detour: 12-factor-apping**

Let’s make our environment a bit more like production. Take a look at [http://12factor.net/config](http://12factor.net/config). This tells us we should keep our configuration in our environment.

To do this, create a file called .env in your project directory.

In it, write:

DATABASE_URL=postgres://localhost:5432/databasename

PORT=3000

This allows a program called Foreman to get variables from this file, and apply them to the code that runs. Foreman is how we simulate running the app on Heroku, so that we can have our local environment be the same as our production environment. Foreman came when you installed the Heroku Toolbelt. We need to create one more file, called Procfile. 

In bash, type touch Procfile (yes, it’s capitalized). In it, add:

web: node app.js

From now on, we’ll launch our app by typing foreman start , which will apply our environment variables and then launch our code. Now your code runs exactly how it will on Heroku.

Also make sure to add .env to your .gitignore file. If you don’t have a .gitignore file, create one now.

## Back to Step 4b

We want to get a database connection that we can re-use for every request so let’s tie a variable, db, to the global scope by declaring it outside of any function, var db;

Next, we’ll connect to postgres, and then make the client available to the *global scope* so that later, it’s sitting around, waiting for us to use. 

pg.connect(conString, function(err, client) {

	db = client;

})

Now you can issue SQL commands to this client! 

## Step 4c: Get the data from the request

There are going to be a lot of instances where we need to get data from the request. Any time someone submits a form, tries to log in, or when analytics data comes in, we need to be able to get it out and do something with it. So let’s explore the ways we can get data from the request.

**Body Parsing**

This is a great time to introduce some more middleware that can help us. As you’ve noticed from learnyounode, parsing the incoming body of a request can be difficult. Let’s cheat, and use a module to help us:

var bodyParser = require('body-parser');

Add this next to logging, but before the static file parsing. 

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

These allow your request body to be easily accessed in the following ways:

**GET requests**

To access parameters that are coming in via GET request (aka, in the querystring), use the following syntax:

req.query["keyname"]

**POST requests**

req.body is populated by the body-parser we just included in our app. Most of the time it includes keys and values, similar to the querystring. Sometimes you’ll need to pull in data that’s more complex than an HTML form’s key-value structure. If so, take a look at [the documentation for how to do that.](http://expressjs.com/4x/api.html#req.body)

**Note: The rest of this tutorial is going to require you to look things up, and accomplish goals, instead of following walkthroughs. It has sample code links, and you should pair program if you get stuck.**

**Step 4d: Insert the data**

**BUT FIRST: check to make sure that the data you got was actually a real email address. Maybe you can use regular expressions ;)**

* With the db we opened on server start, send it some SQL

    * That SQL should be an insert statement, filled in with the data from the request

    * An example: [https://github.com/TradecraftEngineering/messagehub/blob/master/app.js](https://github.com/TradecraftEngineering/messagehub/blob/master/app.js)

    * You’re looking for db.query, which takes the following arguments:

        * SQL query string

        * Parameters to dynamically insert into the parameters ($1, $2, etc) which is an array.

        * A function that executes after the query is finished.

* Serve the "got it" response, but before the query comes back (IE, put the res.end() outside of the callback function.

## Step 4e: Give Back

We want to be able to get all of the users back out of the database, and see them as a response. Define a new route that returns JSON containing all of the email addresses. Call it "/users".

* Query the data the same way we did an INSERT, but this time we’re doing a SELECT statement

    * example: https://github.com/TradecraftEngineering/messagehub/blob/master/app.js

* Once the database returns the data, send it out as a response

## Step 5: Rendering Views and EJS

EJS is a simple way to serve HTML files with content from the database. You can include variables in your HTML, and then your server can replace the variables with actual strings before it’s sent out. An example is displaying a list of users. Pretend we have a list of users that looks like this:

var users = [

	{

		"name" : "John Smith",

		"occupation" : "Conspiracy Nut Who Lives In His Van"

	},

	{

		"name" : "Gary Johnson",

		"occupation": "Part of the secret shadow government",

	}

];

And we want to embed them in our HTML, so that we can see them and their occupations. We can render a template and pass in this variable like this:

response.render("userlist", {"users" : users});

Provided we have an EJS file called userlist.ejs that looks like this:

<% for (var i=0; i < users.length; i++){ %>

	<div class="user"><%=users[i].name%> spends their days as a <%=users[i].occupation%></div>

<% } %>

To use the middleware, use app.set('view engine', 'ejs');

This sets up response.render() to be able to read and render views that are written in EJS.

Resources:

[http://robdodson.me/how-to-use-ejs-in-express/](http://robdodson.me/how-to-use-ejs-in-express/)

[EJS Syntax](http://www.embeddedjs.com/)

## Step5a: EJS

* Use EJS to:

    * Return a page from a .ejs file. Within the file, have an HTML table that contains all of the emails you’ve collected, as well as all of the other columns on that table.

<table>

	<tr>

	<td>Email</td>

	<td>Timestamp</td>

	</tr>

	<tr>

		<td><%=user.email%></td>

<td><%=user.timestamp%></td>

</tr>

</table>

## Step5b: Rendering EJS

Using the rows we got from your database call earlier, inject that data into the template:

Use res.render(‘view_file_name’, { "emails" : emails } )

Which will replace the variables in your HTML with actual strings.

This should allow you to create a page that has dynamic data, instead of just example data.

# Step 6: Send Some Mail

Emails in your table should have a last_emailed field. If they don’t (or something similar) add that now with [an alter table statement.](http://www.postgresqltutorial.com/postgresql-alter-table/)

We also want to know where they are in the sequence of emails, so make sure there is a sequence column as well. 

Create a script called mailer.js. We’ll be using this script, rather than our webserver, to send mail. This is because we want to keep scripts organized by actual function, and the web server should only respond to requests, rather than send mail.

## Step 6a: Sending the initial email

[Take a look at this gist for code that sends email using mandrill.](https://gist.github.com/lizTheDeveloper/2970290ed2223a4a560b) Use the API key provided to send a test email to the emails you’ve saved in your table. **Important: Don’t send more than 5 or so emails, because the amount of emails we get for free is limited and we only have one API key. Also don’t share that gist, because it contains our API key.**

* Write a query that returns all users who don't have anything in the last_email_sent field.

* Send an email to those users using the mandrill API

* Update the database each time you send an email, set the last_email_sent field to the current time, but make sure the database call doesn't block the next email being sent.

**Step 6b: Sending Many Emails**

Adapt your script to send different emails, depending on where a user is in the sequence. This will require that you look at the emails you get back from the database, as well as the sequence and the timestamp. 

* Write a query that will return you every user that hasn't been sent an email in the past 24 hours and is in the second step in the sequence.

    * Send a second email to these users

    * Update the last_email_sent field

* Write a query that will return every user at the third step, that hasn't been sent an email in the past week

    * Send a third email to these users

    * Update the last_email_sent field

## Step 6c: Sending emails from files

* Create a file for each email you want to send, and keep them in a mail_templates folder. 

    * Call them something that contains the sequence number, like email_1.html

* Write a function that creates an email message body from a file, instead of writing it inline. 

    * Make it so your function takes a sequence number as it's argument

    * Your function should return the message body in a callback

    * Send the mail in the callback, using the messageBody you just got from the function.

Example:

function messageBodyFromSequence(sequence, callback){

	// Use the sequence to look for a file with that sequence number in it

	//  Store that file's contents as a variable (call it something like messageBody)

	// call a callback with the contents of the file as an argument:

	callback(messageBody)

}


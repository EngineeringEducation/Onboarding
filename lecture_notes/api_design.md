# API design

## Common Topics:
* APIs are a way for other programmers to use a system you've written
* It means Application Programming Interface
* People use it, and it's an interface, so user interface design is really what we're doing
* When designing APIs, they should be:
	* Designed for Humans To Use
	* Flexible
	* Based on Use Cases
	* Have Good Docs
	* Hide as much implementation detail from the user as possible

## Examples:
* [REST APIs](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) - from [Roy Fielding's dissertation](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
* [The Document Object](https://developer.mozilla.org/en-US/docs/Web/API/document)
* [Some iOS examples]


## REST API design
* REST means REpresentational State Transfer
* Roy Fielding wrote it in 2000, so the ramifications of these ideas are still being worked out
* Basically it works like this:
	* You have a client, and a server
	* The client needs to get resources from the server
		* Resources are things; tweets, events, friends, orders
		* They can also be collections of things; timelines, friends' lists, order history
		* But it depends on what might typically be useful; user with order history, user with friends' list and timeline, photo with share statistics and user
	* The client sends a request to the server, along with any other information the server might need to serve the request, which might include
		* Parameters; user_id, a search term, start and end dates for a query
		* Authentication information; so the server can serve protected resources to the client
		* The current state of the client, so the server can serve state-dependant information; pagination information, model updates, or new resrouces to be created
	* The server compiles and returns the information and the client does something with it; updates the view, validates the response, terminates the connection
* Designing a good REST API
	* First start by identifying resources you want to expose
		* Determine some use-cases for your API. Anyone using it is a "user" and you are creating an "interface" so use good interface design principles. 
		* Make a list of resources you would need in each use-case
			* Viewing a list of all tweets for people you follow
				* Tweets
				* Users that made those tweets
				* Share stats for each tweet
				* Timestamp information
			* Seeing a list of recent changes to an article
				* Article
				* Article versions
				* Users that versioned the article
			* Seeing users active in the system now with links to the resource used to send them a notification (like for uber)
				* Users active
				* Notification resource link
				* User availability
		* See what general resources are are needed across use-cases
	* Define endpoints for those resources, or for common use cases
		* resources
			* /user/:user_id
			* /:user_name/tweet/:tweet_id
			* /articles/:article_id
	* Document those endpoints
		* What methods are available? ; GET, POST, PUT, DELETE
			* Use the right method for the specific action you're trying to do
			* GET only to recieve information, never to change it
			* POST to create new information
			* PUT to update existing information
			* DELETE to delete
		* What information do you need in order to make this request?
			* User's ID, not just username?
			* Requests should be able to take in information the user actually has- if you don't normally expose user IDs but you do expose Username, that information should be unique enough to get it.
		* Do you need special permissions / are these resources protected?
			* IE does the client have to be authenticated to get it?
			* Does the client have to request those permissions from the user?
		* Show an example request
		* Provide an example response to that request
	* [Follow best-practices](http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

	* REST API Examples
		* [Instagram API Docs](https://instagram.com/developer/)
		* [Google Drive API Docs](https://developers.google.com/drive/v2/reference/)
		* [Uber API Docs](https://developer.uber.com/v1/endpoints/)
		* [All of the rest of them](http://www.publicapis.com/)

	* REST API Resources
		* [Modeling Resources](http://www.thoughtworks.com/insights/blog/rest-api-design-resource-modeling)
		* [Express tutorial to build one yourself](https://scotch.io/tutorials/build-a-restful-api-using-node-and-express-4)
		* [Best Practices](http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

## Building Module APIs

* http://mattgemmell.com/api-design/
* http://lcsd05.cs.tamu.edu/slides/keynote.pdf
* http://devdocs.io/

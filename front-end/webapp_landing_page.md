# Webapp Landing Page


## Phase 1
Front-end  
**Skills needed:**  
* HTML/CSS
* Basic Javascript
* Basic DOM Manipulation
* HTML Forms
* Bootstrap

Alright! So we got a lot of signups on Betali.st and have gotten great feedback from our user testing of our alpha release. Time to get a signup screen together.   

~~Our service is pretty brittle~~ We move fast and break things, so we probably can't handle the amount of users that are going to sign up. We're going to have to implement some kind of queue like mailbox.app did when they launched. They were really popular, and I think it was because of that giant line. Everyone in San Francisco loves lines.  

Get together a landing page, [use our colorscheme](http://www.colourlovers.com/palette/148712/Gamebookers) to implement a place where users can sign up, and then are automatically placed in line. We don't really want to keep track of the line anywhere, so just put some random numbers on the page that increment with Javascript.  

Also install Google Analytics.  

Collect these things about the user:  
* First Name / Last Name
* Email
* Password

Submit the info to the `/submit` endpoint.  

This should take you less than a day, so have it live before lunch tomorrow.  

## Phase 2
Front-end  
**Skills Needed:**  
* API Integration
* AJAX
* HTML/CSS
* Basic Javascript
* Basic DOM Manipulation
* Bootstrap

Ok people are apparently upset that we didn't use real numbers in our virtual line, so we should probably actually put the real numbers on the page. Submit an AJAX request to our server at `/submit`. It will return an object that looks like this:  
```javascript
{
	"user_id" : 7890,
	"total_signups" : 9123,
	"users_accepted" : 6789
}
```

On the page, tell the user what number they are in line (user_id), how many people are ahead of them (user_id - users_accepted), and how many people are behind them (total_signups - user_id).

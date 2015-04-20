# User Authentication

## Cookies and Routes
* Set a cookie from a form value
	* `req.body["name"]`
	* `res.cookie("name", "value")` - gets sent to browser, then back with every request
* Make the cookies secure with a secret key
	* `app.use(cookieParser(process.env["COOKIE_SECRET_KEY"]));`
	* Remember to keep the key in the `.env` file / environment - changing it will log everyone out
* Create a login route
	* Create a cookie on the server IF the credentials check out
* Save the logged in status in a secure cookie
	* Later you can access it with every subsequent request with `req.signedCookies["key"]`
* Use middleware to authenticate some routers but not others
	* `router.use(function(req, res, next) {})` - login credential check goes here, on the router
* Save the user's status on the request, so it is portable across functions
	* `req.user = req.signedCookie["user_id"]`
	* If you're doing this, make sure to encrypt the cookie, so the user can't change it.

## Credentials
* Use something unique that only the user has
	* That can be a password 
	* Can be something else unique, like a bearer token from oAuth
	* Something only the user/someone trusted on their behalf has access to
		* [This module can help you implement user auth from oAuth providers](http://passportjs.org/guide/)
	* A pair of things is usually sufficient, username, password
		* Like an address, and a key
	* Locks can be picked- use two-factor authentication for better security
* Encryption
	* `[protected form] = [salt] + protect([protection func], [salt] + [credential]);`
	* [The Crypto Module](https://nodejs.org/api/crypto.html)
* Storage
	* [Use this cheatsheet](https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet)
	* _NEVER EVER_ store plaintext passwords, log passwords with console.log, or transmit unencrypted passwords (ie, from server to database - encrypt before you send!)
* Logging
	* Anytime credentials are changed needs to be logged
	* Failed credentials should be logged
	* [Follow this cheatsheet to see what you should log](https://www.owasp.org/index.php/Logging_Cheat_Sheet)

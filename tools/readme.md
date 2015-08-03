# Developer Tools

## Bash
* [Learn Command Line the Hard Way](http://cli.learncodethehardway.org/)
* [Explain Shell](http://explainshell.com/) - paste commands in this box to see what they do

## Git
* [Basic Git](./GitOperations)
* [Try Git]

## Heroku
In order to deploy a web application from your machine to Heroku, we need to follow the principles in [the 12 factor app](http://12factor.net/). This means:
* Your app should be runnable by [Foreman](https://github.com/ddollar/foreman)
  * Have a [Procfile](http://blog.daviddollar.org/2011/05/06/introducing-foreman.html) that defines your process types
  * Ensure any connection strings (database URLS) or any other URLs in the app are stored in environment variables and accessed that way
  * Ensure API keys are also stored as environment variables and are accessed that way

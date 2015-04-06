# Project 1: Personal Brand Website

This project is to get you familiar with the idea of starting a project from scratch. This is to help you with the idea of starting something that you own, quickly. We’ve got some requirements this has to satisfy, but most of the decisions are up to you. Since you get to decide things, we’re going to take a look at the types of decisions you need to make, and how you might make them. There are suggestions in this document, but you don’t have to take those decisions. Just make sure you can explain why you made the decision.

Before we get started, let’s take a look at what we’re trying to build, and what it needs to be able to do.

This is your personal brand website. It should convey who you are, both in terms of concrete details (your name, a photo of you) and in how you you think (hobbies, interests, writing you’ve done and links to other internet representations of you). It should also show off your mad skills in the arena of front-end web. This isn’t to say you need to have a lot of really hard problems to solve on this basic static website, it should just display that you know how to do, or figure out how to do, the things you need to know in order to make a website happen. 

## Super-Serious Requirements

Your site should:

* Be in HTML, CSS, and JavaScript
* Be made up of static files
* Not be created using a WYSIWYG editor or 1-click solution (like squarespace)
* Have information people might need to know about you
    * name and photo
    * contact information
    * interests, background
    * portfolio links (if you have one)
* Be hosted on Github Pages
* Be "pretty"
* Be mocked up first, marked up second
* Not be needlessly complicated, because we’re fast and agile

Your track leads will take a look at each one and tell you if you’ve met these requirements. These requirements are a bit "fuzzy", like you would get from a normal stakeholder, so interpret them however you need to in order to make your stakeholders happy.

## Getting Started - Mock It Up before Marking It Up

Let’s get started by looking at some of the decisions you need to make in order to do this.

First, what will your site look like? This is a good time to sketch this out on paper. Draw some general layout ideas on a whiteboard, or jump into your favorite image editor and move boxes around. However it is you tend to get your visual ideas out of your brain and in front of your face, create something that helps you visualize it.

Second, test your idea. This is the most important part of every single project forever. Show your mockups or designs to someone else, preferably someone who isn’t another engineer. Someone who might end up using your site to find you- ask them what they would think! If the answer is "Uhh, I would be really confused as to what you’re trying to convey to me", maybe it’s time to go back to the drawing board. They might have thoughts about your design choices, but as long as those thoughts aren’t “ow, my eyes”, this project is a form of self-expression, so just watch for what you convey to people with those choices, and see if it expresses who you are accurately.

## Hello World

Follow [the instructions for Github Pages here](https://pages.github.com/), since that’s where we’re going to be hosting your site. You’re creating a "User or Organization" site, so follow those instructions. Once you have a git repository up, and you’ve pushed your hello world to the internet, and you’ve verified it works by visiting it, it’s time to get started actually coding your site.

## A wild decision appears!

Now that it’s time to actually turn your mockup into markup, we’re going to use another tool to make this quick and easy. This requires you to make your very first technical decision, which is **what kind of framework do you want to use for the CSS?** Writing CSS files from scratch might build character, but we’re all impressive characters already so let’s just skip the newbie stuff and jump right into what the pros use. Pick a framework to help you lay things out with the minimum of fuss. I like these:

* [Bootstrap](http://getbootstrap.com/)
* [Foundation](http://foundation.zurb.com/)
* [Gumby](http://gumbyframework.com/)

There are many more, googling "css frameworks" will present you with a plethora of choices. But how do you make a decision on these frameworks? Factors to consider are:

* Speed of installation: some are very simple to install and start using. Others require more time to configure.
* Dependency: Some frameworks require a lot of other things (ruby, compass, etc) to use, and tend to complicate things in order to add a lot of abstraction.
* Ease of understanding: Can you jump right in and use it? Will it slow you down? Does it make sense to use in the short or medium term, or only in the long term? (This is a short-term project that you’ll continue to build upon.
* Integration with other systems - does it play nicely with other components we’re going to use? Since we’re not really going to use many other components, this isn’t a big deal.
* Best long-term support: Do lots of people use the framework? Is it still supported, by dedicated developers? If it’s not owned by anyone anymore, it’s hard to make the case that it will integrate nicely and continue to work for you into the future, even in the short-term.

For your first project, I highly suggest going with Bootstrap, since it doesn’t require any compilation, and there are many [CDNs](http://en.wikipedia.org/wiki/Content_delivery_network) readily available ([here’s one now!](http://www.bootstrapcdn.com/)). 

Once you’ve picked a framework, [include it on your front page.](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Why_use_CSS) Then, commit that code. _Notice how we’re committing every time we solve a problem?_ This is a great habit to get into- every time you get something working that wasn’t before, it’s time to commit, and push.

## Confronting Your Choices

Now, look at the documentation for your framework. They’re going to include a [grid system](http://getbootstrap.com/css/#grid) (look at the examples), which is a way of laying things out in columns without worrying about how to align things or keep things in the right order. Done correctly, this makes your code really readable. 

Start dividing up your mockup into rows and columns, by drawing boxes over the layout. Even if your design is less grid-like and more flow-y, try drawing your mockup on grid paper, and you’ll see what I mean. Then, create those "boxes" by placing `div`s on your pages with the appropriate `row` and `column` classes. 

An example in bootstrap:
```html
<div class="row">
  <div class="col-md-8">I’m an 8-column div</div>
  <div class="col-md-4">I’m a 4-column div to the right of the 8 column div</div>
</div>
<div class="row">
  <div class="col-md-4">I’m a 4 column div, in a new row, so I’m below the first two divs</div>
  <div class="col-md-4">I’m in the same row, so I’m to the right of the first div in this row.</div>
  <div class="col-md-4">I feel like those other divs explained things pretty well.</div>
</div>
```
This should give you an idea of how to structure your page. Create the "bones" of the page (the main structure divs), and add the content you had in mind (or [some lorem ipsum](http://slipsum.com/)). Now would be a great time to commit your changes, and push them to github!

## The Part With Style

Once you’ve lain out your page the way you want, it’s time to add the colors, additional styles, and other assets that will make your page pretty. Add an additional page-specific stylesheet. Add your classes in here, and remember you are probably going to come back and change this page radically. Make it easy to find things, and leave yourself notes explaining what classes and styles are for. Remember you can comment using `/* this syntax. */`.

Remember to have the CSS documentation open as you lay things out. Mozilla’s documentation is best, it’s canonical and they have an [exhaustive reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) next to [in-depth tutorials](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started). If you get stuck, or aren’t sure how to achieve an effect, that’s what Track Leads (and your classmates) are for.

## When am I done?

Done? What does that mean? Look, this is your page to show the universe that you know what you’re doing. Once you feel like it accurately displays the skills you already have, push a *little* further to make those skills a little more advanced. **Once you feel proud of the work you’ve done, you’re ready to publish it**. This page will never be *done*, you’ll always be coming back to it to show off that you’ve understood more things, and you’ll also be adding works to your portfolio section as you have more to show off. You’ll be showing this off to *the entire student body (of engineering)* when you feel done, so just stop when you’re ready to do that.


Exercise Git: Version Control
=======

First, make a Github account. I recommend using your twitter username if available. Next, follow [this tutorial](https://help.github.com/articles/set-up-git/) to set up git on your computer to be connected to Github.

After you've run through that, head over to the folder you've used to hold code you completed in the prework. You should probably have subfolders in that folder, one for each exercise or project you've done. In your most recent project, run the following commands:   
```shell
$ git init
```
This creates a new `git` _repository_, or _repo_, which is like a database that saves every change you make to a line in a file. It remembers what line and what characters you change, with what changes you make, so that if two people work on the same file it can easily merge the two files together. You don't have to run this command more than once in a folder, because the folder is now a repository. It's like the folder gains new commands, in addition to `ls`, `cd`, `pushd` and `popd` you can now run a multitude of commands beginning with the word `git`.  

`git init` should only happen on a "project", not on all your folders. Never try to make a `git` repository in a folder above one that already has a `git` repo. Here's an example -  
~/src/exercises/exercise01 - if this folder has a repository in it (type `git status` to see)  
~/src/exercises - this folder should NOT have `git init` run in it, because you can't create repositories inside of other repositories (or you can, but shouldn't). You should have a repository for each project you do.  

Next, `git` doesn't know what files you want it to track, so we're going to have to tell it. 
`touch readme.md` will create a file in this directory, but it will be blank. You'll need to put something in it with the `subl` command - so type `subl readme.md` and add some text. This will be visible to the world soon, so put something you're OK with people seeing that describes what you're working on.  

Now on to adding files.  
`git add readme.md` will add the readme file you just made to `git`'s database, and tell it to save it next time you "commit". `git` now knows about the file, but you haven't told `git` to save the most recent copy. Let's do that now with `git commit -m'Initial Commit'`.

We need to break down that command, so let's look at the pieces.  
    `git` is the program we're using to keep track of versions of files.  
    `commit` saves a version of everything you've added to the commit as it is right now.  
    `-m''` is a flag that means "message". It takes an argument, which is what those '' are for. Inside the '' ("" is also fine) you put a message describing what you did to the file, or files. Something like "added sort function" or "fixing typos on homepage", which summarizes the task you were trying to accomplish. This helps when you need to go back and figure out what you did, or when you need to find an example of a time when you wrote something. It's essentially notes to yourself, or to your team.

This brings us to the next part, where you might have to actually share code - either with people, or just between computers. What we're going to do is create a "remote". The nice thing about keeping our changes line-by-line and character-by-character is that we can just send all of those changes to another computer, apply them in order, and reconstruct the whole file. Then, if you make a change, all you have to do is send the change. The way we send these changes is by establishing a remote. 

First, we need to create a remote repository to add. Head back over to http://github.com/, and be sure you're logged in.  
Next, click "create repository" anywhere you can find a button to do so, or go to https://github.com/new to make a new repository. Under "Repository Name", enter Exercise01 (or whatever you'd like call it, but note this affects the URL). The description is optional. Leave it set to Public, because Private repositories cost money. Don't check "initialize this repository with a README". Click "Create Repository".  
You'll see a screen that says "Quick Setup" - click the HTTP button (next to where it says "SSH"). You'll see an address that says something like `https://github.com/[username]/Exercise01.git` - copy this url. 
This is the address of the _remote_ (because it's on a different server) git repository we're going to add to our local repository.

When we add a remote, much like when we do any other configuration, it only exists for that repository. Outside of the folder our repository is in, none of these settings exist. Let's try adding our remote to our repository:  
`git remote add origin https://github.com/[your username goes here]/Exercise01.git`

Now we have a remote - this is like a portal that goes to whatever URL we point at. Let's break down that command.  
`git remote` refers to the part of the git program that allows us to add a list of URLs that we can send and receive code from. This is kind of like a cross between a bookmark and an FTP server.   
`origin` This is a nickname for the remote. We can put ANY word here we want - Liz personally uses "github", but it's common on the Internet to see "origin" used for github.  
`https://github.com/[your username goes here]/Exercise01.git' should reference a URL that is either a github repository you've already created, like the one we've created earlier.

So, now that we've established a portal link, what do we do with it? Same thing you'd probably do if you actually opened a portal to the server room at Github. Push things through it and see what happens.  

`git push origin master`  

See how we referenced origin there? That's the nickname of the portal - it tells `git` what portal to mischievously push things through. You might wonder about what "master" means - that's the name of the branch. For now, we'll have only one branch, so we'll always type master there. In the Further Reading section, there's some information about branching.  

Once you've typed `git push origin master` git will ask you for a username - this is the username you signed up with github under. Then, it will ask for a password. When you type, you may be used to seeing asterisks(*) appear, but nothing will show up instead of just displaying your password for the world to see - so don't worry about typing it in in front of your partner.  

After this, head over to your Github profile. You should see your new repo has been created, and any files you've added should have been pushed to the server. This is the simplest way to back up your work to the cloud, share code between teams, and make sure you remember what you did, when you did it, with notes to yourself.  

Now, run through this exercise to make sure you understand what you've done.

http://try.github.com

Further Reading
========

Information about Branching  
http://pcottle.github.com/learnGitBranching/  

Here's a very through overview of Git and how it works.  
http://ftp.newartisans.com/pub/git.from.bottom.up.pdf  

Even more through, is this book:  
http://git-scm.com/book/en  

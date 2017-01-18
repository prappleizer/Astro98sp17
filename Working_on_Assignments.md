# Working on Assignments 

Every week, the tutorial you will be working on (in ipynb format) will be added to the Astro 98 git repository in a new directory. Here's the easiest way to interface with the tutorials. 

1) First, you will need to clone the class git repository to your personal computer. You do not need a github account for this step, but it is a good way to be backing up and tracking your work in general (not just in this class). Either way, start by navigating to the directory on your computer where you want the class files to be located, make sure you are connected to the internet, and type: 
```
git clone https://github.com/prappleizer/Astro98sp17.git
```
This should clone the the class repo onto your computer. (That is, if you type ```ls``` in terminal you should now have an Astro98sp17 folder there). 

2) This directory is what is known as "git enabled," which means that when we put a new assignment onto github, all you have to do is go to Astro98sp17/ on your computer and type 
```
git pull
```
to get the most recent version/any new files or tutorials we have uploaded.

## If you want your own github to work with

1) If you want to get practice using git and backing up your work online, go to ```http://www.github.com``` and sign up for an account.

2) Once you are logged into your account, click the link to make a new repository. Name it something like astro-sp17 (or whatever). In the options to make the repository, you will have to leave the repo public unless you want to pay money, and you will want to leave the box for "initialize with a readme" UNCHECKED (you will be importing an existing repository). 

3) Back on your computer, within the Astro98sp17 directory, type
```
 git remote rename origin pydecal
```
and then 
```
 git remote add origin <URL_OF_YOUR_REPO>
```
where the url is the one that pops up when you click "clone or download" in the top left corner of your github repository online. 

4) Now, you are set up and ready to go. When you pull things, it comes from our repository of files, and when you push things, they go into your own directory. Here is an example of a typical workflow:
```
cd Astro98sp17
git pull 
# make any changes to files, etc
git add . #or add specific files if thats all you want to push up
git commit -m 'brief description of your edits'
git push -u origin master
```
At which point, your terminal will ask you for your github username and password. 


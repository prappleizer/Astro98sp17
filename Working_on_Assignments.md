# Working on Assignments 

Every week, the tutorial you will be working on (in ipynb format) will be added to the Astro 98 git repository in a new directory. Here's the easiest way to interface with the tutorials. 

1) First, you will need to clone the class git repository to your personal computer. You do not need a github account for this step, but it is a good way to be backing up and tracking your work in general (not just in this class). Either way, start by navigating to the directory on your computer where you want the class files to be located, make sure you are connected to the internet, and type: 
```
git clone https://github.com/prappleizer/Astro98sp17.git
```
This should clone the the class repo onto your computer. (That is, if you type ```ls``` in terminal you should now have an Astro98sp17 folder there). 

2) This directory is what is known as "git enabled," which means that when we put a new assignment onto github, all you have to do is ```cd Astro98sp17``` on your computer and type 
```
git pull
```
to get the most recent version/any new files or tutorials we have uploaded.

## To complete Homework 0

Once you have done the git clone step, do the following commands:

1) 
```
source activate pydecal #if it isn't already
cd Astro98sp17/tutorials/hw0
```

2)
```
jupyter notebook hw0.ipynb
```


#Turning in Assignments for Python Decal

You will be getting the files you need for the class by git pulling them, and you will be submitting them using the okpy infrastucture. For the first few tutorials, this will be built in, and you won't have to worry about it, and once the tutorials shift out of ipython notebooks we will show you how to submit via okpy (it's an easy one line command).



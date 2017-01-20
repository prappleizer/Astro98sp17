# Astro 98/198 [Python Decal] Spring 2017

##Setting up your computer/data environment for this class. 

##MAC OSX

1) First things first. Your terminal program allows you to type commands to control your computer. On a Mac, you can open the Terminal by going to your Applications screen and selecting Terminal (it might be in the folder named “Other”). Or, you can open Spotlight (Cmd + Space) and type “Terminal”.

2) First, let’s install ```brew``` if you haven’t done that yet. Homebrew is a program that allows you to easily install other software on OSX. In your terminal, run:
```
# This downloads the Ruby code of the installation script and runs it
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Verify your installation by making sure brew --version doesn’t error at your terminal.

3) Next, install ```wget```. This is a command-line tool that lets you download files / webpages at the command line.
```
 # Uses Homebrew to install wget
 brew install wget
```
4) Download the Anaconda installation script (if you do not already have anacondas distribution of python on your computer:
```
 # Uses wget to download the installation script, naming it install_anaconda.sh
 wget -O install_anaconda.sh https://repo.continuum.io/archive/Anaconda3-4.2.0-MacOSX-x86_64.sh
```
5) Install Anaconda:
```
 # Run the installation script
 bash install_anaconda.sh
```
Restart your terminal at this point (not just closing the window, but quitting the application from the bar) and then reopening.
Ensure the installation worked by running ```conda --version```.

6) Run these commands to create a new conda environment. Each conda environment has its own package versions. This allows us to switch between package versions easily. For example, this class uses Python 3.5, but you might have another that uses Python 2.7. With a conda environment, you can switch between those at will.
```
 # Create a conda env called pydecal that uses python 3.5
 conda create --name pydecal python=3.5

# Switch to the pydecal environment
source activate pydecal

 # Install the packages for this class
 conda install -n pydecal jupyter pandas numpy matplotlib
 pip install okpy
```
From now on, you can switch to the pydecal env with ```source activate pydecal```, and switch back to the default env with ```source deactivate```.

7) Now, use brew to install the latest version of git by running:
```
 brew install git
```
Check you have the latest version by typing ```git --version```. It should be 2.5.0 or higher. 
You may remove the ```install_anaconda.sh``` script now if you’d like since it’s quite large.

To continue to the next part (setting up the assignments directory), click here: http://github.com/prappleizer/Astro98sp17/blob/master/Working_on_Assignments.md 

## Windows 

1) Visit https://www.continuum.io/downloads#windows and download the installer for Python 3.5. Download the 64-bit installer if your computer is 64-bit (more likely), the 32-bit installer if not. You can Google how to check whether your computer is 64 or 32 bit.

2) Leave all the options as default (install for all users, in the default location). Make sure both of the checkboxes (add to path, register) are checked.

3) Install.

4) Verify that the installation is working by starting the Anaconda Prompt (you should be able to start it from the Start Menu) and typing ```python```:

5) Run these commands to create a new conda environment. Each conda environment has its own package versions. This allows us to switch between package versions easily. For example, this class uses Python 3.5, but you might have another that uses Python 2.7. With a conda environment, you can switch between those at will.
```
 # Create a conda env called pydecal that uses python 3.5
 conda create --name pydecal python=3.5

 # Switch to the pydecal environment
 activate pydecal

 # Install the packages for pydecal
 conda install -n pydecal jupyter pandas numpy matplotlib
 pip install okpy
```
From now on, you can switch to the pydecal env with ```activate pydecal```, and switch back to the default env with ```deactivate```.

### Installing git 

1) You might already have ```git``` installed. Type ```git``` at the Anaconda Prompt. If that works, then you can skip these steps. 

2) If step one didn't work, at the anaconda prompt, type:
```
 # Use anaconda to install git
 conda install -c anaconda git -y
```

3) Now, verify that git is installed by typing ```git --version``` on the command line. 

To see how you will be obtaining and submitting your homework for this class, please 

To continue to the next part (setting up the assignments directory), click here: http://github.com/prappleizer/Astro98sp17/blob/master/Working_on_Assignments.md 

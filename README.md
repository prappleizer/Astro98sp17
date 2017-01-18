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
Ensure the installation worked by running ```conda --version```.

6) Run these commands to create a new conda environment. Each conda environment has its own package versions. This allows us to switch between package versions easily. For example, this class uses Python 2.7, but you might have another that uses Python 3. With a conda environment, you can switch between those at will.
```
 # Create a conda env called pydecal that uses python 2.7
 conda create --name pydecal python=2.7

# Switch to the pydecal environment
source activate pydecal

 # Install the packages for this class
 conda install -n pydecal jupyter pandas numpy matplotlib
 pip install okpy
```
From now on, you can switch to the pydecal env with ```source activate ds100```, and switch back to the default env with ```source deactivate```.

7) Now, use brew to install the latest version of git by running:
```
 brew install git
```
Check you have the latest version by typing ```git --version```. It should be 2.5.0 or higher. 
You may remove the ```install_anaconda.sh``` script now if you’d like since it’s quite large.


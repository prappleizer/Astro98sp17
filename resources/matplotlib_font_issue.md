# Fixing the Matplotlib font import error

For many of you (and for myself), there has been a strange bug that pops up when opening ipython, of the form
```
/Users/ipasha/anaconda2/lib/python2.7/site-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
Using matplotlib backend: TkAgg
```

This is not a major issue, and doesn't cause any specific problems while you are working, but it does take ipython an annoying few extra seconds to load and is annoying to have pop up every time. I have discovered what seems to be a fix, so you can follow the following steps if you'd like to get rid of it: 

1) Navigate to the matplotlib cache directory. On a Mac, this will probably be
```
cd ~/.matplotlib
```

2) ls the files in the directory. There should be one or two ```.cache``` files. Make a test directory by typing 
```
mkdir test
```
and then move the following files into it by typing 
```
mv fontList.cache test
mv matplotlibrc test #if this file exists for you
```

3) Open a new terminal window and launch ipython by typing
```
ipython
```

It might take a while the first time, because it is now creating a new cache file. But after it loads, try exiting ipython by typing ```exit``` and then restarting ipython as above, and hopefully you'll find that it loads faster and doesn't spit out that error message. 

Good luck!

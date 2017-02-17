#Homework 4 Skeleton File
import numpy as np 
import matplotlib.pyplot as plt 



def load_data(data_file):
	'''
	A function to load a data file containing columns (x,y) into two separate lists
	PARAMS
	---------
	data_file (str): Path location of a data file to be loaded

	RETURNS
	---------
	x_array (np.array): array with all the x values from the file
	y_array (np.array): array with all the y values from the file
	'''
	#Your code here


	return x_array, y_array


#Run your function to load the data below and plot it to see what it looks like. Then comment out the plots so you can keep going forward


##############


def linear_fit(x,y):
	'''
	A function to perform a linear least squares fit to a set of data. 
	PARAMS
	----------
	x (arr): array of x values to be fit 
	y (arr): array of y values to be fit

	RETURNS
	---------
	(c1,c2) (tuple): Tuple containing the two fit parameters (slope and intercept)

	'''
	#your code here



	return c1, c2


def plot_fit(x,y,____):
	'''
	A function to create a y-array (same len as x,y) containing the fit evaluated at the x-array values. Optionally plot the fit over the data. 
	PARAMS
	---------
	x (arr): array of x values to be fit 
	y (arr): array of y values to be fit
	do_plot (optional): defaults to False, but can be set to True to plot the fit line over the data and show. 
	'''
	plt.ion() #sets matplotlib into interactive mode so that the plots will pop up but the code will keep going
	#Your code here 
	#you'll probably be running your linear fit function in here

	#if the do_plot option is true, do the plots (NICELY!)
	
	
	return x, y_fit #you can change the name of y_fit to whatever you define, or use y_fit in your function



def find_residuals(x,y,____):
	'''
	A function to calculate the residuals between a set of y-values and the fit values for the corresponding x values. Optionally plots residuals. 
	PARAMS
	---------
	x (arr): the x-array of the data (only needed for plotting purposes)
	y (arr): the y-array of the data
	do_plot (optional): defaults to False, but can be set to True to plot the residuals

	RETURNS
	---------
	residuals (arr): array of the residuals for each pair of y values 
	residual_stat (dict): dictionary containing keys 'mean', 'std', 'min', and 'max' describing the statistics of the residual array
	'''
	plt.ion() #sets matplotlib into interactive mode so that the plots will pop up but the code will keep going
	#Your code here
	#You'll probably be running your plot_fit function here (with plotting turned off), since you'll need y_fit
	#calculate residuals

	#plot them, if do_plot is True

	

	residual_stat = {}
	#set keys and values via dictionary indexing

	return residuals, residual_stat






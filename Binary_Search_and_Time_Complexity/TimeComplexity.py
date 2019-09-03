"""
This file plots the time versus input size plot for binary and linear search

"""
import matplotlib.pyplot as plt
from Search import LinearSearch, BinarySearch
import time
import random

def ForLinearSearch():
	x, y = [], []
	for i in range(10000 , 100000, 10000):
		values = [random.randint(0, i) for r in range(i)]
		start = time.time()
		LinearSearch(values, values[len(values)-1])
		end = time.time()
		difference = end - start	# difference is the time taken for the search algorithm to run
		x.append(i)
		y.append(difference)

	plt.plot(x,y)
	plt.show()

def ForBinarySearch():
	x, y = [], []
	for i in range(10000 , 100000, 10000):
		values = [random.randint(0, i) for r in range(i)]
		values.sort()
		start = time.time()
		BinarySearch(values, values[len(values)-1])
		end = time.time()
		difference = end - start
		x.append(i)
		y.append(difference)

	plt.plot(x,y)
	plt.show()

ForLinearSearch()
ForBinarySearch()
"""
This file contains the implementation for linear and binary search

"""
def LinearSearch (elements, searchParameter):
	i = 0
	while True:
		if searchParameter == elements[i]: # if the element we are searching for matches the element in the list,
										   # we return the index of the array 
			index = i
			break
		i = i + 1
	return index

def BinarySearch(elements , searchParameter): # requires sorted array 
	maxi = len(elements) - 1
	mini = 0
	i = int((maxi + mini)/2)

	while searchParameter != elements[i]: # the value of i is halved each time and maxi and mini are two positions 
										  # that denote the maximum and minimum which search parameter cannot exceed  
		if elements[i] < searchParameter:
			mini = i
		else:
			maxi = i
		i = int((maxi + mini)/2)
	return i



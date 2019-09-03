import random 
import time
import matplotlib.pyplot as plt

def InsertionSort(A):

	for i in range(1,len(A)):
		j = i - 1
		content = A[i]
		while(j >= 0 and A[j] > content):
			A[j+1] = A[j]
			j = j - 1
		A[j+1] = content
	return A 

x = []
y = []

for i in range(1000, 10000, 1000):
	A = [random.randint(0, i) for r in range(i)]
	start = time.time()
	InsertionSort(A)
	end = time.time()
	difference = end - start
	x.append(i)
	y.append(difference)
	print("The time taken for execution is {0}", difference)

plt.plot(x,y)
plt.show() 

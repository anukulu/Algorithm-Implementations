import random 
import time
import matplotlib.pyplot as plt

def Merge(L, leftSize, R, rightSize, A):
	i=0
	j=0
	k=0
	while(i < leftSize and j < rightSize):
		if(L[i] < R[j]):
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
		k = k + 1
	
	while(i < leftSize):
		A[k] = L[i]
		k  = k + 1
		i = i + 1
	while(j < rightSize):
		A[k] = R[j]
		j = j + 1
		k = k + 1

def MergeSort(A, n):
	
	if (len(A) <2):
		return

	mid = int(len(A)/2)

	L =	[A[s] for s in range(0,mid)]
	R = [A[s] for s  in range(mid, n)]

	MergeSort(L, len(L))
	MergeSort(R, len(R))
	Merge(L, len(L), R, len(R), A)

x = []
y = []

for i in range(100000, 1000000, 100000):
	A = [random.randint(0, i) for r in range(i)]
	start = time.time()
	MergeSort(A, len(A))
	end = time.time()
	difference = end - start
	x.append(i)
	y.append(difference)
	print("The time taken for execution is {0}", difference)

plt.plot(x,y)
plt.show() 


	

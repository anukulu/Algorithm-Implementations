eventsThatHappen = []
indexOfEvents = []
indexRecursively =[]

events = [[1,2],[3,4],[0,6],[5,7],[8,9],[5,9]]

def EventsSort():
	for j in range(1,len(events)):
		key = events[j]
		i = j-1
		while(i >= 0 and key[1] < events[i][1]):
			events[i+1] = events[i]
			i-=1
		events[i+1] = key

def ActivitySelectionIterative(allEvents , index):
	eventsThatHappen.append(allEvents[index])
	indexOfEvents.append(index)
	currentEvent = eventsThatHappen[len(eventsThatHappen)-1]
	for i in range(1 , len(allEvents)):
		if(currentEvent[1] <= allEvents[i][0]):
			eventsThatHappen.append(allEvents[i])
			indexOfEvents.append(i)
			currentEvent = allEvents[i]
	return(indexOfEvents)

def ActivitySelectorRecursive(allEvents , k, n):
	s = [x[0] for x in allEvents]
	f = [x[1] for x in allEvents]
    m = k + 1
    while (m<n and s[m]<f[k] and k>=0):
        m = m + 1
    if (m < n):
        indexRecursively.append(m)
        ActivitySelectorRecursive(allEvents, m , n)
    else:
        return None
    return indexRecursively    

EventsSort()
print(events)

index = input("Select the index for the event : ")
print("By iteration : ")
print(ActivitySelectionIterative(events,int(index)))
print("By recursion : ")
print(ActivitySelectionRecursive(events,-1, len(events))



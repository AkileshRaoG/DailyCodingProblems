#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def ProcessList(inputList , valueToCheck):
	lenOfList = len(inputList)
	quickSort(inputList, 0, lenOfList-1)
	first = 0
	last = lenOfList-1

	while first < last :
		if (inputList[first] + inputList[last] == valueToCheck):
			return 1
		elif (inputList[first] + inputList[last] < valueToCheck):
			first += 1
		else:
			last -= 1
	return 0

def quickSort(inputList, firstIndex, lastIndex):
	if firstIndex < lastIndex:
		index = splitList(inputList, firstIndex, lastIndex)
		quickSort(inputList, firstIndex, index-1)
		quickSort(inputList, index+1, lastIndex)

def splitList(inputList, firstIndex, lastIndex):
	element = inputList[lastIndex]
	index = firstIndex-1
	for x in xrange(firstIndex,lastIndex):
		if inputList[x] <= element:
			index += 1
			inputList[index], inputList[x] = inputList[x], inputList[index] #fastest way to swap elements
		inputList[index+1], inputList[lastIndex] = inputList[lastIndex], inputList[index+1]
	return index+1

#Test1
list1 = [1,7,2,4,10,15] 
k = 16
if (ProcessList(list1, len(list1), k)): 
    print("True") 
else: 
    print("False")

#Test2
list2 = [1,-4,20,6,11,5] 
k = 16
if (ProcessList(list2, len(list2), k)): 
    print("True") 
else: 
    print("False")

#Test3
list3 = [1,4,45,6,10,-8] 
k = 16
if (ProcessList(list3, len(list3), k)): 
    print("True") 
else: 
    print("False")



			

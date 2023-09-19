myList=[85,24,63,45,17,31,96,50]
for index in range(len(myList)-1):
    print(myList)
    nextMinValue=myList[index+1]
    for unsortedIndex in range(index+1,len(myList)):
        if myList[unsortedIndex] < nextMinValue:
            nextMinValue= myList[unsortedIndex]
    if nextMinValue < myList[index]:
        nextMinIndex = myList.index(nextMinValue)
        myList[nextMinIndex]= myList[index]
        myList[index]= nextMinValue
print(myList)

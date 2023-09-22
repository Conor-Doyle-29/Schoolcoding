myList=[8,8,9,5,10,6,3]
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

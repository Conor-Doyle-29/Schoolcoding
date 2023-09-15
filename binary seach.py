myList = [17,24,31,45,40,63,85,96]
myList.sort()  
def binarysearchloop(listIn,key):  # Define a binary search function using a loop
    first = 0  # Initialize variables to keep track of the search range
    last = len(listIn)-1
    while (last - first) >=0: # Loop until the search range is valid
        middle= first+((last-first)//2) # Calculate the middle index of the current search range
        if listIn[middle] == key: # Check if the key is at the middle position
            return middle
        elif key< listIn[middle]:  # If the key is less than the middle element, update the last index
            last= middle-1
        else:  # If the key is greater than the middle element, update the first index
            first= middle+1
    return -1  # Return -1 if the key is not found in the list
print(binarysearchloop(myList, 85 ))

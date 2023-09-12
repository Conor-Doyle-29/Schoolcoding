myList=[85,24,62,45,17,31,96,50]
key=28
for index in range(len(myList)):
    if myList[index]==key:
        location = index

print("key found at:", location)
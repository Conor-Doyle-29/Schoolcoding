myList= [85,24,63,45,17,31,96,17]
occurences = []
def linearSearch(listIn,key):
    
    for index in range(len(listIn)):
        if listIn[index] == key:
            occurences.append(index)
    return occurences        
 
print(linearSearch(myList,1))

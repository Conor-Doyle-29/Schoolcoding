myList = [ 85,24,63,45,17,31,96,50] #creates a list
key = 17  # delcares a varibale that lets the program know
for index in range(len(myList)): # starts a for loop that goes through the whole lenght of the list 
  if myList[index] == key:  # checks to see if the current i is the key 
    location = index  # if it is makes location = the i 
print("Key found at:",location)  # prints results 
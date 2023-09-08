def addition (numIn):
   
    if numIn >1 :
        return numIn + addition(numIn-1)
    elif numIn==1:
        return 1
    else:
        return 0
numIn= int(input("number:"))
ans = addition(numIn)
print(ans)
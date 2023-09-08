def factorial (numIn):
   
    if numIn >1 :
        return numIn * factorial(numIn-1)
    else:
        return 1 
ans = factorial(5)
print(ans)
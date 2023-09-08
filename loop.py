def factorial(numIn):
    base=1
    fact=numIn
    
    if fact >1:
        for num in range(numIn,1 ,-1 ):
            fact= fact*(num-1)
    else:
        return base 
        
    return fact
numIn=2

print(factorial(numIn))
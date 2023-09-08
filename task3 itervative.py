def additon(numIn):
    base=1
    fact=numIn
    
    if fact >1:
        for num in range(numIn,1 ,-1 ):
            fact= fact+(num-1)
    elif fact ==1:
        return base 
    else:
        return 0 
        
    return fact
numIn= int(input("Whats your number nerd?:"))

print(additon(numIn))
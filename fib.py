def fib(n): # define the function
  if n <= 1: # checks if it is zero 
    return n #returns 0 
  # checks if n is one or 2 return 1 
    
  else:
    return fib(n-1)+fib(n-2) # fib(n-1)

y = int(input("Enter a number: "))
ans = fib(y)
print(ans)
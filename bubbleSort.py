def isPrime(number):
  for i in range(2, number):
    if number % i == 0:
      return False
  return True

 

for i in range(2, 1000):
  result = isPrime(i)
  if result == True:
    print(i)

 

number = int(input("Enter a number: "))
print("This number is prime:", isPrime(number))
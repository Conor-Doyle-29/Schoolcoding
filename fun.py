import random

mylist = []

for i in range(0,1000000000):
    x = random.randint(1,100)
    mylist.append(x)

print(mylist)
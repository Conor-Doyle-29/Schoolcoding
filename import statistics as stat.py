import statistics as stat
import matplotlib.pyplot as plt 
import collections 
file=open("tmp.csv","r")
dataIn=file.read()
file.close
print(dataIn)
list= dataIn.split(",")
list.remove(list[-1])
print(list)

mean1= stat.mean(list)
print(mean1)

median1 = stat.median(list)
print(median1)

mode1=stat.mode(list)
print(mode1)

frequency1 = collections.Counter(list)
print(frequency1)

plt.plot(list)
plt.show()
import os
import matplotlib.pyplot as pt

x=[]
y=[]
readFile=open("Points.txt","r")
data=readFile.read().split("\n") #Getting Each Coordinate
for a in data:
    arr=a.split(",")
    x.append(int(arr[0]))
    y.append(int(arr[1]))
pt.plot(x,y)
pt.show()

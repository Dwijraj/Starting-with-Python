import matplotlib.pyplot as plt

fig=plt.figure()       # Helps Create Figure

"""
Next Two Lines help to set the back ground color
"""
rect=fig.patch
rect.set_facecolor('green')
"""
facecolor is background of graph
"""
x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]
x2=[0,4,7,10]
y2=[2,5,7,9]
x3=[6,7,8,18]
y3=[5,8,99,109]
graph1=fig.add_subplot(2,1,1,facecolor='black')
graph1.plot(x,y,'red',linewidth=4.0)
graph1.plot(x2,y2,'yellow',linewidth=2.0)
graph1.plot(x3,y3,'orange',linewidth=6.0)
"""
tick_params changes the marker color on the axis
"""
graph1.tick_params(axis="x",color="white")
graph1.tick_params(axis='y',color='white')
"""
Spines is the border of the graph
"""
graph1.spines["top"].set_color('w')
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')
graph1.spines["bottom"].set_color('w')
"""
Change label color
"""
graph1.set_title('Random Graph',color='white')
graph1.set_xlabel('This is X',color='white')
graph1.set_ylabel('This is Y',color='white')

graph2=fig.add_subplot(2,1,2,facecolor='black')
graph2.plot(x,y,'red',linewidth=4.0)
graph2.plot(x2,y2,'yellow',linewidth=2.0)
graph2.plot(x3,y3,'orange',linewidth=6.0)
"""
tick_params changes the marker color on the axis
"""
graph2.tick_params(axis="x",color="white")
graph2.tick_params(axis='y',color='white')
"""
Spines is the border of the graph
"""
graph2.spines["top"].set_color('w')
graph2.spines["left"].set_color('w')
graph2.spines["right"].set_color('w')
graph2.spines["bottom"].set_color('w')
"""
Change label color
"""
graph2.set_title('Random Graph',color='white')
graph2.set_xlabel('This is X',color='white')
graph2.set_ylabel('This is Y',color='white')

plt.show()

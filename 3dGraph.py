from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig=plt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')
X=[1,2,3,4,5]
Y=[6,7,8,9,10]
Z=[11,12,13,14,15]
chart.plot_wireframe(X,X,X)
plt.show()

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
fig=pt.figure()
rect=fig.patch
rect.set_facecolor('black')

chart=fig.add_subplot(1,1,1,projection='3d')
X=[1,2,3,4,5,6,7,8]
Y=[2,5,3,8,9,5,6,1]
Z=[3,6,2,7,5,4,5,6]

Xx=[-1,-2,-3,-4,-5,-6,-7,-8]
Yy=[-2,5,-3,8,-9,5,-6,1]
Zz=[3,-6,2,-7,5,-4,5,-6]


chart.scatter(X,Y,Z,c='red',marker='o')
chart.scatter(Xx,Yy,Zz,c='blue',marker='^')
chart.set_xlabel('x_axis')
chart.set_ylabel('y_axis')
chart.set_zlabel('z_label')
pt.show()

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
import numpy as np
fig=pt.figure()
chart=fig.add_subplot(1,1,1,projection='3d')

pos=np.arange(6)+0.5

x,y,z=axes3d.get_test_data(0.05)

dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

chart.plot_wireframe(x,y,z,rstride=10,cstride=10)
chart.set_xlabel('X label')
chart.set_ylabel('Y label')
chart.set_zlabel('Z label')

pt.show()

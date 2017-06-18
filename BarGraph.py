import matplotlib.pyplot as plt
import numpy as np

pos=np.arange(6)+0.5
arr=['Avi','h','h','yu','jh','qwe']
plt.barh(pos,(4,8,12,3,17,6),align='center',color='red')

plt.xlabel('Height in inches',color='red')
plt.ylabel('Students',color='r')
plt.title("Heights of students in inches",color='blue')
plt.tick_params(axis='x',colors='white')
plt.tick_params(axis='y',colors='white')
plt.yticks(pos,arr)          
plt.show()

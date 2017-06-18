import matplotlib.pyplot as plt
import numpy as np
sizes=[50,23,15,7,5]
labels=["Android","Apple","Windows","Blackberry","Xiaomi"]
colors=['red','yellow','orange','cyan','Magenta']
plt.pie(sizes,colors=colors,startangle=90,labels=labels)
plt.axis('equal')
plt.legend(title='Legend',loc='lower left')
plt.title("Pie Chart")

plt.show()

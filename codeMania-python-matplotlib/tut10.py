import matplotlib.pyplot as plt

import  numpy as np

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

font1={'family':'serif','color':'black','size':'20'}
font2={'family':'serif','color':"red","size":'29'}
plt.plot(x,y)

plt.title("MAGA Point",fontdict=font1,loc='right')
plt.xlabel("azure network",fontdict=font2)
plt.ylabel("project insight",fontdict=font2)
plt.grid(color='red',linestyle='-',lw= 2)


plt.show()
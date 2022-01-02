import matplotlib.pyplot as plt 
import numpy as np

# plot 1

x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

y=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

# plt.subplot(1,2,1)
# plt.plot(x, y)
# plt.title('income')

# # plot 2

# x=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y=np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

# plt.subplot(1,2,2)
# plt.plot(x,y)
# plt.title("grenade")

# plt.suptitle('megatron')
plt.scatter(x,y)

plt.show()
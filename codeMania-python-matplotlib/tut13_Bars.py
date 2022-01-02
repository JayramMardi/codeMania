# chapter bars ploting [matplotlib]

'''
from numpy.lib.polynomial import polyfit


Creating Bars

With Pyplot, you can use the bar() function to draw bar graphs:
'''

import matplotlib.pyplot as plt

import numpy as r 
x=r.array(["A","D","F","G","H","J","K","L"])
y=r.array([2,3,4,5,6,7,8,9])

plt.bar(x,y)
plt.show()

# The bar() function takes arguments that describes the layout of the bars.

# The categories and their values represented by the first and second argument as arrays.

u=(["apple","banana"])
p=([450,900])

plt.title("GROCERY CHART",c="red")

plt.bar(u,p)
plt.show()

m=(["A","D","F","G"])

# Horizontal Bars

#If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

m=(["apple","banana","grapes","mangoes"])
n=([2,3,4,5])

plt.barh(m,n)
plt.show()

#Bar Color

# The bar() and barh() takes the keyword argument color to set the color of the bars:

o=(["apple","banana"])
p=([1,900])

plt.barh(o,p,color="#7a69cf")
plt.show()

# Color Names

# You can use any of the 140 supported color names.

'''
Bar Width

The bar() takes the keyword argument width to set the width of the bars:
'''


o=(["apple","banana","citrus fruit","mangoes"])
p=([779,900,455,766])

plt.bar(o,p,width=0.1)
plt.show()

#The default width value is 0.8

'''
The default width value is 0.8

Note: For horizontal bars, use height instead of width.
'''
#  Bar Height 


# The barh() takes the keyword argument height to set the height of the bars:

q=(["apple", "banana","watermelon","mangoes"])
w=([3, 8, 1, 10])

plt.barh(q,w, height=0.8 )

plt.show()


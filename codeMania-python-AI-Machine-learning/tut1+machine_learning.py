# mean median mode
'''
what can we learn from looking at a group of numbers?

In Machine Learning (and in mathematics) there are often three values that interests us:

    Mean - The average value
    Median - The mid point value
    Mode - The most common value

Example: We have registered the speed of 13 cars:

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
'''
import numpy as  r 
from scipy import stats   

speed= [32,35,232,323,434,544,644,644,644]

o=r.median(speed) #mean or for mode use it import stats from scipy  
print(o)

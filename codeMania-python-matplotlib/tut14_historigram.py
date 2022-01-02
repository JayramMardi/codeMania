# Matplotlib Histograms 

'''
Histogram

A histogram is a graph showing frequency distributions.

It is a graph showing the number of observations within each given interval.

Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
'''
import  matplotlib.pyplot as plt
import numpy as r 

x=r.random.normal(170,10,250)
plt.hist(x)
plt.show()

p=r.random.normal(170,10,250)
plt.hist(p)

plt.show()


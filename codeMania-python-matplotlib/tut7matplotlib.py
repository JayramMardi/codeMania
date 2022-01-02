# Chapter matplotlib pyplot
'''
Pyplot

Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
import matplotlib.pyplot as plt

Now the Pyplot package can be referred to as plt.
Example

Draw a line in a diagram from position (0,0) to position (6,250):
'''

import sys
import matplotlib 

# matplotlib.use('agg') Don't use this line because this makes code un run

import matplotlib.pyplot as plt
import numpy as r



xpoint=r.array([0,6])
ypint=r.array([0,340])

plt.plot(xpoint,ypint)
plt.show()

#Two  lines to make our compiler able to draw:

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


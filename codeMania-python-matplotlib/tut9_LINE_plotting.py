'''
Chapter Matplot lining ....

Linestyle

You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:
Example

Use a dotted line:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
'''



import  matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6,5,7])
y=np.array([1,2,4,5,5,6,])

plt.plot(y,ms=34,marker='*',mec='#ccffff',mfc="#ccffff",linestyle=':')

plt.show()
'''
Example

Use a dashed line:

plt.plot(ypoints, linestyle = 'dashed')

'''
import matplotlib.pyplot as plt
import numpy as np


p=np.array([3,8,1,10])

plt.plot(p,marker='*',mec='r',mfc='r',ms=20,ls='dashed')
plt.show()
'''
Shorter Syntax

The line style can be written in a shorter syntax:

linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.
'''

'''
Line Width

You can use the keyword argument linewidth or the shorter lw to change the width of the line.

The value is a floating number, in points:
Example

Plot with a 20.5pt wide line:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np


p=np.array([3,8,1,10])

plt.plot(p,marker='*',mec='r',mfc='r',ms=20,ls='dashed',color='hotpink',lw='20.5')
plt.show()

'''
Multiple Lines

You can plot as many lines as you like by simply adding more plt.plot() functions:
Example

Draw two lines by specifying a plt.plot() function for each line:
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
'''


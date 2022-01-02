#  chapter Matplotlib Plotting

'''
The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
'''
# Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import  numpy as r
import sys



x=r.array([1,9,])
y=r.array([4,10])

plt.plot(x,y)
plt.show()

'''
Plotting Without Line

To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.
'''

x=r.array([3,10])

y=r.array([0,34])

plt.plot(x,y,'o')
plt.show()

'''
Multiple Points

You can plot as many points as you like, just make sure you have the same number of points in both axis.
Example

Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):f
'''

x=r.array([1,2,4,9])
y=r.array([3,6,8,10])

plt.plot(x,y,label="red")
plt.show()


#Two  lines to make our compiler able to draw:

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

'''
Default X-Points

If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3, (etc. depending on the length of the y-points.

So, if we take the same example as above, and leave out the x-points, the diagram will look like this:
'''
# Plotting without x-points:

ypoints=r.array([0,2,3,5,6,7,99])

plt.plot(ypoints)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


# CHAPTER Matplotlib Markers
'''
Markers

You can use the keyword argument marker to emphasize each point with a specified marker:
'''
x=r.array([0,3,5,6,8,9])

y=r.array([2,4,6,7,8,10])

plt.plot(x,y,marker="*")

plt.show()

'''
Marker Reference

You can choose any of these markers:
Marker 	Description
'o' 	Circle 	
'*' 	Star 	
'.' 	Point 	
',' 	Pixel 	
'x' 	X 	
'X' 	X (filled) 	
'+' 	Plus 	
'P' 	Plus (filled) 	
's' 	Square 	
'D' 	Diamond 	
'd' 	Diamond (thin) 	
'p' 	Pentagon 	
'H' 	Hexagon 	
'h' 	Hexagon 	
'v' 	Triangle Down 	
'^' 	Triangle Up 	
'<' 	Triangle Left 	
'>' 	Triangle Right 	
'1' 	Tri Down 	
'2' 	Tri Up 	
'3' 	Tri Left 	
'4' 	Tri Right 	
'|' 	Vline 	
'_' 	Hline 	
'''

'''
Format Strings fmt

You can use also use the shortcut string notation parameter to specify the marker.

This parameter is also called fmt, and is written with this syntax:
marker|line|color
Example

Mark each point with a circle:
'''
x=r.array([3,5,5,6,7,8])
y=r.array([1,3,5,6,7,8])

plt.plot(x,y,'-.r')
plt.show()

'''
The marker value can be anything from the Marker Reference above.

The line value can be one of the following:
Line Reference
Line Syntax 	Description
'-' 	Solid line 	
':' 	Dotted line 	
'--' 	Dashed line 	
'-.' 	Dashed/dotted line 	
Note: If you leave out the line value in the fmt parameter, no line will be plottet.
'''

'''
Color Reference
Color Syntax 	Description
'r' 	Red 	
'g' 	Green 	
'b' 	Blue 	
'c' 	Cyan 	
'm' 	Magenta 	
'y' 	Yellow 	
'k' 	Black 	
'w' 	White
'''
'''
    Marker Size

You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:
'''


x=r.array([1,3,4,5,9,5])
y=r.array([0,3,6,8,8])

plt.plot(x,marker='o',ms='17')
plt.show()

'''
Marker Color

You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
Example

Set the EDGE color to red:
'''
x=r.array([2,3,5,6])
y=r.array('[0,3,5,6,8]')

plt.plot(x,marker='*',ms=34,mec='r')
plt.show()

'''
You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
Example

Set the FACE color to red:
'''

x=r.array([1,3,5,6])
y=r.array([2,3,5,6])

plt.plot(x,marker='*',ms=34,mfc='r')
plt.show()
'''
# Use both the mec and mfc arguments to color of the entire marker:
# Example

# Set the color of both the edge and the face to red:
'''
import matplotlib.pyplot as plt
import numpy as r

y=r.array([0,4,6,7,7,8])

plt.plot(y,marker='*',ms=30,mec='r',mfc='r')
plt.show()

'''
You can also use Hexadecimal color values:
Example

Mark each point with a beautiful green color:
...
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
... 
'''

import  matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6,5,7])
y=np.array([1,2,4,5,5,6,])

plt.plot(y,ms=34,marker='*',mec='hotpink',mfc="hotpink",linestyle=':')

plt.show()


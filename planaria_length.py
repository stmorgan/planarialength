filename = '12.1_H.jpg'               # Enter filename of planarian image. 

%matplotlib tk                       
import math                          # Math Library
import matplotlib.pyplot as plt      # Plotting Library
import matplotlib.image as mpimg     # Image plotting library

points = []                                    # For accumulating points in length path. 
fig = plt.figure(figsize=(20,30))              # Create figure handle
img=mpimg.imread('images/jpgs/' + filename)    # Read image from file. 

def line_length(points):                       # Calculate length of path described by points array. 
    if len(points) <= 1:                       # Return length 0 for single point in path array. 
        return 0.0
    else:
        length = 0.0                           # Zero length accumulator. 
        for i in range(len(points)-1):         # Iterate through points in path array. 
            x1 = points[i][0]                  # Extract descriptive variables from path array. 
            y1 = points[i][1]
            x2 = points[i+1][0]
            y2 = points[i+1][1]
            length += math.sqrt((x2-x1)**2 + (y2-y1)**2)    # Add length of next path segment to path array.
        return length

def onclick(event):                            # Record position of mouse clicks on planarian length path. 
    global points                              # Declare global path array for use in click event function.

    ix, iy = event.xdata, event.ydata          # Convert to descriptive variables. 
    plt.scatter(x=[ix], y=[iy], c='r', s=40)   # Draw clicked points on planarian image. 
    plt.show()                                 # Update image (show it.)

    points.append([ix, iy])                    # Add new points to path array. 
    ll = line_length(points)                   # Get total length of path. 
    plt.title('Length: ' + str.format('{0:.0f}', ll))    # Display length in plot title field. 
    print(ix, iy, ll)                          # Print point and path length to console. 
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)   # Connect click event with handling function. 
imgplot = plt.imshow(img)                      # Plot initial image. 
plt.show()  

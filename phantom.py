# Step 1: 2D Mesh Point calculation

face  = [
    [1, 1, 0], # c1
    [3, 1, 0], # c2
    [2, 2, 0],
    [3, 2, 0],
    [1, 3, 0],
    [2, 3, 0]
]

phantom = []
inface = []
gridset = []

def max(inlist):
    max = inlist[0]
    for i in inlist:
        if(i > max):
            max = i
    return max

def min(inlist):
    min = inlist[0]
    for i in inlist:
        if(i < min):
            min = 1
    return min

xmax = max([c[0] for c in face])
ymax = max([c[1] for c in face])
xmin = min([c[0] for c in face])
ymin = min([c[1] for c in face])

A1 = (xmin, ymin)
B1 = (xmax, ymin)
E1 = (xmin, ymax)
X1 = (xmax, ymax)

print(A1, B1, E1, X1)
grid_size = (4, 4, 0)
ugrid_size = (grid_size[0]+1,grid_size[1]+1,grid_size[2]+1)

for z in range(ugrid_size[2]):
    for y in range(ugrid_size[1]):
        for x in range(ugrid_size[0]):
            gridset.append([x, y, z])

for c in gridset:
    if(A1[0] <= c[0] <= B1[0] and A1[1] <= c[1] <= E1[1]):
        inface.append(c)

# inface = output

# Step 2: Point Conversion

tdp2 = []

for c in inface:
    tdp1 = []
    tdp1.append(c[0])
    tdp1.append(c[1])
    tdp2.append(tdp1)

#print(tdp2)

g2 = []

for c in gridset:
    g1 = []
    g1.append(c[0])
    g1.append(c[1])
    g2.append(tdp1)

#print(tdp2)

# Step 3: Color calculation:
print(tdp2)
white = [255, 255, 255]
black = [0, 0, 0]

out = []

for y in range(ugrid_size[1]):
    xout = []
    for x in range(ugrid_size[0]):
        coord = [x, y]
        w = False
        for c in tdp2:
            if(c == coord):
                w = True
        if(w):
            xout.append(white)
        else:
            xout.append(black)
    out.append(xout)

# Step 4: Rendering:

from PIL import Image
import numpy as np

Image.fromarray(np.uint8(out)).convert('RGB').save('2drend.png')
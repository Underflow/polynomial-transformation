#! env python2.7
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

c1 = [] # Class 1
c2 = [] # Class 2
for _ in range(100):
    # Create a random distribution for the first class
    angle = np.random.rand() * 2 * math.pi
    dist = np.random.random()
    (x, y) = (dist * math.cos(angle), dist * math.sin(angle))
    c1.append((x,y))
    plt.scatter(x, y, alpha=1)

    # Random distribution of the second class
    angle = np.random.rand() * 2 * math.pi
    dist = 1 + np.random.random()
    (x, y) = (dist * math.cos(angle), dist * math.sin(angle))
    c2.append((x, y))
    plt.scatter(x, y, alpha=1, c=[1,0,0])

# Display the non-linearly separable space in 2d
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Apply a polynomial transform on the previous distributions
for (x, y) in c1:
    ax.scatter(x, y, x **2 + y ** 2, alpha=0.5, c='r', marker='o')
for (x, y) in c2:
    ax.scatter(x, y, x **2 + y ** 2, alpha=0.5, c='b', marker='o')

# Display the linaryly separable space in 3d
plt.show()

import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from scipy.spatial import KDTree
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cosine
from scipy.spatial.distance import hamming
import matplotlib.pyplot as plt

points = np.array([
    [2,4],
    [3,4],
    [3,0],
    [2,2],
    [4,4]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:,1], simplices, label = "Bibekster")  # The simlices property creates a generalization of the triangle notation.
plt.scatter(points[:,0], points[:,1], color = 'r')
plt.legend()
plt.show()

# Convex Hull 
points = np.array([
    [2,3],
    [3,4],
    [3,0],
    [2,2],
    [4,1],
    [1,2],
    [5,0],
    [3,1],
    [1,2],
    [0,2]
])

hull = ConvexHull(points)   # it returns the smallest polygon containing all the points
hull_points = hull.simplices  # it is a pair of indices that defines one of the edges of the hull.

plt.scatter(points[:,0], points[:,1]) # plots all the points
for simplex in hull_points:  # plots the convex hull's edges
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.legend()
plt.show()

# KDTree
points = [(1,-1),(2,3), (-2,3), (2,-3)]
kdtree = KDTree(points)   # It returns a KDTree object
res = kdtree.query((1,1))   # It returns distance to the nearest neighbour
print(res)

# Euclidean Distance
p1 = (1,0)
p2 = (10,2)
res = euclidean(p1, p2)
print(res)

# Cityblock Distance (Manhattan Distance)
p1 = (1,0)
p2 = (10,2)
res = cityblock(p1, p2)
print(res)

# Cosine Distance
p1 = (1,0)
p2 = (10,2)
res = cosine(p1, p2)
print(res)

# Hamming Distance
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)





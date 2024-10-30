import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order

arr = np.array([[0,1,2],[1,0,0],[2,0,0]])
arr1 = csr_matrix(arr)
print(connected_components(arr1))

# Dijkstra
arr = np.array([[0,1,2],[1,0,0],[2,0,0]])
arr1 = csr_matrix(arr)    # since there are zero elements we call this method
print(dijkstra(arr1, return_predecessors= True, indices= 0))  # Here the predecessors would return the node before the current node. indices 0 means that the source node in node0

# Floyd Warshall
arr = np.array([[0,1,2],[1,0,0],[2,0,0]])
arr1 = csr_matrix(arr)
print(floyd_warshall(arr1, return_predecessors= True))

# Bellman Ford
arr = np.array([[0,-1,2],[1,0,0],[2,0,0]])
arr1 = csr_matrix(arr)
print(bellman_ford(arr1, return_predecessors= True, indices=0))

# Depth First Order
arr = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
arr1 = csr_matrix(arr)
print(depth_first_order(arr1,1))

# Breadth First Order
arr = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0],[0,1,0,1]])
arr1 = csr_matrix(arr)
print(breadth_first_order(arr1, 1))

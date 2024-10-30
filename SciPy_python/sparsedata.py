import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0,1,1,1,0,2])
print(csr_matrix(arr))

# Viewing stored data (not the zero items) with the data property:
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr).data)

# Counting nonzeros with the count_nonzero() method:
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(arr).count_nonzero())

# Removing zero-entries from the matrix
arr = np.array([[0,0,0],[0,0,1],[1,0,2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

import numpy as np

def input_matrix(rows, cols, matrix_name="Matrix"):  # Takes user input for a matrix with given rows and columns.
    print(f"Enter the elements of {matrix_name} row by row (space-separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}:").split()))
        if len(row) != cols:
            print(f"Error: Please enter exactly {cols} elements")
            return None
        matrix.append(row)
    return np.array(matrix)

# Taking input for Matrix A
rows_A = int(input("Enter the number of rows for Matrix A: "))
cols_A = int(input("Enter the number of columns for Matrix A: "))
A = input_matrix(rows_A, cols_A, "Matrix A")
print("Matrix A:\n", A)

# Taking input for Matrix B
rows_B = int(input("Enter the number of rows for Matrix B: "))
cols_B = int(input("Enter the number of columns for Matrix B: "))
B = input_matrix(rows_B, cols_B, "Matrix B")
print("Matrix B:\n", B)

# Basic Matrix Operations

addition = A + B
print("Addition of the matrix:\n", addition)
subtraction = A - B
print("Subtraction of the matrix:\n", subtraction)
multiplication = A * B   # Element wise
print("Multiplication of the matrix:\n", multiplication)
dot_product = np.dot(A,B) 
print("Dot product of the matrix:\n", dot_product)
determinant_A = np.linalg.det(A)
determinant_B = np.linalg.det(B)
print("Determinant of A:\n", determinant_A)
print("Determinant of B:\n", determinant_B)

# Matrix Inversion
if determinant_A != 0:
    inverse_A = np.linalg.inv(A)
    print("The inversion of matrix A is:\n", inverse_A)
else:
    print("Matrix A does not have a inversion\n")

if determinant_B != 0:
    inverse_B = np.linalg.inv(B)
    print("The inversion of Matrix B is \n", inverse_B)
else:
    print("Matrix B does not have an inversion\n")

# Finding the Eigen values and Eigen Vectors

eigenvaluesA, eigenvectorsA = np.linalg.eig(A)
eigenvaluesB, eigenvectorsB = np.linalg.eig(B)
print("Eigenvalues of A:\n", eigenvaluesA)
print("Eigenvectors of A:\n", eigenvectorsA)
print("Eigenvalues of B:\n", eigenvaluesB)
print("Eigenvectors of B:\n", eigenvectorsB)

# Solving a system of Linear equations:

coefficients = np.array([[3, 2], [1, 4]])
constants = np.array([8, 7])

print(type(coefficients))
print(type(constants))

solution = np.linalg.solve(coefficients, constants)
print("solution of the system of equations:", solution)




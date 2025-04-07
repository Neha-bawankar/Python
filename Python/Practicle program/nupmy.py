import numpy as np

# Create a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix:")
print(matrix)

# Perform element-wise operations
squared = matrix ** 2

print("\nElement-wise Squared Matrix:")
print(squared)

# Apply broadcasting (adding a row vector to each row in the matrix)
row_vector = np.array([10, 20, 30])
broadcasted_result = matrix + row_vector
print("\nBroadcasted Result:")
print(broadcasted_result)

# Compute the matrix transpose
transpose = matrix.T
print("\nMatrix Transpose:")
print(transpose)

# Perform matrix multiplication
identity = np.eye(3)  # Identity matrix
multiplication_result = np.dot(matrix, identity)
print("\nMatrix Multiplication Result:")
print(multiplication_result)

# Calculate eigenvalues and eigenvectors (linear algebra example)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)

# Reshape the matrix
reshaped = matrix.reshape(1, 9)
print("\nReshaped Matrix (1x9):")
print(reshaped)
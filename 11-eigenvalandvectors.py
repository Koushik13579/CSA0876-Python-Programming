import numpy as np
matrix = np.array([[1, 2], [3, 3]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

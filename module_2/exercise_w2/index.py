import numpy as np

# length of a vector
def compute_vector_length(vector):
    return np.linalg.norm(vector)

# vector1 dot vector2
def compute_dot_product(vector1, vector2):
    return np.dot(vector1, vector2)

# matrix1: m x n
def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# matrix inverse
def compute_matrix_inverse(matrix):
    return np.linalg.inv(matrix)

# eigenvector and eigenvalue
def compute_eigenvector_and_eigenvalue(matrix):
    return np.linalg.eig(matrix)

# consine similarity
def compute_cosine_similarity(vector1, vector2):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
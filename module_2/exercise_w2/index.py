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


vector = np.array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print(round(result, 2))

v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))

x = np.array([[1, 2], [3, 4]])
k = np.array([1, 2])
print('result \n', x.dot(k))

x = np.array([[-1, 2], [3, -4]])
k = np.array([1, 2])
print('result \n', x@k)

m = np.array([[-1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multiplication(m, v)
print('result \n', result)

m1 = np. array([[0, 1, 2], [2, -3, 1]])
m2 = np. array([[1, -3], [6, 1], [0, -1]])
result = matrix_multiplication(m1, m2)
print(result)

m1 = np.eye(3)
m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1@m2
print(result)

m1 = np.eye(2)
m1 = np. reshape(m1, (-1, 4))[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)

m1 = np. array([[1, 2], [3, 4]])
m1 = np. reshape(m1, (-1, 4), "F")[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)

m1 = np. array([[-2, 6], [8, -4]])
result = compute_matrix_inverse(m1)
print(result)

matrix = np. array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvector_and_eigenvalue(matrix)
print(eigenvectors)

x = np. array([1, 2, 3, 4])
y = np. array([1, 0, 3, 0])
result = compute_cosine_similarity(x, y)
print(round(result, 3))

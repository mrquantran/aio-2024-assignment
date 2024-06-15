import numpy as np
from support import is_number


@is_number
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


@is_number
def relu(x):
    return np.maximum(0, x)


@is_number
def elu(x, alpha=0.01):
    return np.where(x < 0, alpha * (np.exp(x) - 1), x)


x = input("Enter a number: ")
try:
    x = float(x)
except ValueError:
    print("Invalid number")
    exit()

print("Choose an activation function: \n1. Sigmoid\n2. ReLU\n3. ELU\n")

activation = input("Enter a number: ")

if activation == '1':
    print(f'Sigmoid({x}) = {sigmoid(x)}')
elif activation == '2':
    print(f'ReLU({x}) = {relu(x)}')
elif activation == '3':
    print(f'ELU({x}) = {elu(x)}')
else:
    print("Invalid activation function")
    exit()



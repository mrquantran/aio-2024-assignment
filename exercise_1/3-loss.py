import numpy as np

def loss_mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def loss_mse(y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))

def loss_rmse(y_true, y_pred):
    return np.sqrt(loss_mse(y_true, y_pred))

# input number samples
while True:
    try:
        num_samples = int(input("Enter number of samples: "))
        break
    except ValueError:
        print("number of samples must be an integer number")
    
# input loss name
print("Choose a loss function: \n1. Mean Absolute Error\n2. Mean Squared Error\n3. Root Mean Squared Error\n")
loss_function_choosing = input("Enter a number: ")

if loss_function_choosing == '1':
    loss_function = loss_mae
elif loss_function_choosing == '2':
    loss_function = loss_mse
elif loss_function_choosing == '3':
    loss_function = loss_rmse
else:
    print("Invalid loss function")
    exit()

#random from 0 - 10
predict = np.random.Generator(0, 10, num_samples) 
target = np.random.Generator(0, 10, num_samples)

print(f'Predict: {predict}')
print(f'Target: {target}')
print(f'Loss: {loss_function(target, predict)}')
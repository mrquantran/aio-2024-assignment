import torch
import torch.nn as nn
import torch.nn.functional as F


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)
        return exp_x / torch.sum(exp_x)


# Testing the implementation
x = torch.tensor([1.0, 2.0, 3.0])
softmax = Softmax()
softmax_stable = SoftmaxStable()

print("Softmax:", softmax(x))
print("Softmax Stable:", softmax_stable(x))
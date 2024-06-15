from support import isNumber

@isNumber
def mean_difference_of_n_root(y, y_hat, n, p=1):
    return (y ** (1 / n) - y_hat ** (1 / n)) ** p


print(mean_difference_of_n_root(y=100, y_hat=99.5, n=2, p=1))
print(mean_difference_of_n_root(y=50, y_hat=49.5, n=2, p=1))
print(mean_difference_of_n_root(y=20, y_hat=19.5, n=2, p=1))
print(mean_difference_of_n_root(y=0.6, y_hat=0.1, n=2, p=1))

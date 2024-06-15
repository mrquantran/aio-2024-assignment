from support import isNumber

@isNumber
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


@isNumber
def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += (-1)**i * x**(2*i + 1) / factorial(2*i + 1)
    return result


@isNumber
def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += (-1)**i * x**(2*i) / factorial(2*i)
    return result


@isNumber
def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += x**(2*i + 1) / factorial(2*i + 1)
    return result


@isNumber
def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += x**(2*i) / factorial(2*i)
    return result


print('sin(3.14) =', approx_sin(3.14, 10))
print('cos(3.14) =', approx_cos(3.14, 10))
print('sinh(3.14) =', approx_sinh(3.14, 10))
print('cosh(3.14) =', approx_cosh(3.14, 10))

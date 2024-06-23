def is_number(func):
    def wrapper(*args, **kwargs):
        for arg, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"{arg} must be number")
        return func(*args, **kwargs)
    return wrapper


def is_greater_than_0(func):
    def wrapper(*args, **kwargs):
        for arg, value in kwargs.items():
            if value < 0:
                raise ValueError(f"{arg} must be greater than 0")

        return func(*args, **kwargs)
    return wrapper

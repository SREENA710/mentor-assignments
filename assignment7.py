# def require_positive(function):
#     @wraps(function)
#     def postive_number(number):
#         if postive_number <= 0:
#             raise ValueError(f"Given number must be positive")
#         else:
#             print(f"Provide a valid number")


def require_positive(func):
    def wrapper(*args, **kwargs):
        if args[0] <= 0:
            raise ValueError("Given number must be a positive number.")
        return func(*args, **kwargs)
    return wrapper
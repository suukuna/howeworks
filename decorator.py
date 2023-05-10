def decorator_allows_return_only_str(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)

    return wrapper


@decorator_allows_return_only_str
def calculate_cylinder_volume(radius, height: int):
    formula = 3.14 * (radius ** 2) * height
    return type(formula)


calculate_cylinder_volume(15, 2)

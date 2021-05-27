def val_checker(func):
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs) > 0:
            return func(*args, **kwargs)
        elif func(*args, **kwargs) < 0:
            raise ValueError('Функция принимает только положительные числа')

    return wrapper


@val_checker
def calc_cube(x: int) -> int:
    return x ** 3

print(calc_cube(2))
print(calc_cube(-3))

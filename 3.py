# если один аргумент
def type_logger(func):
    def wrapper(*args, **kwargs):
        return {func(*args, **kwargs): type(func(*args, **kwargs))}

    return wrapper


@type_logger
def calc_cube(x: int) -> int:
    return x ** 3


print(calc_cube(4))


# если аргументов несколько
def type_logger(func):
    def wrapper(*args, **kwargs):
        return {i: type(i) for i in func(*args, **kwargs)}

    return wrapper


@type_logger
def calc_cube(*args):
    for i in args:
        yield i ** 3


print(calc_cube(1, 2, 3, 66, 11, 22))


# если аргументы именованные
def type_logger(func):
    def wrapper(*args, **kwargs):
        return {i: type(i) for i in func(*args, **kwargs)}

    return wrapper


@type_logger
def calc_cube(**kwargs):
    for i in kwargs.values():
        yield i ** 3


print(calc_cube(first=9, second=11, third=90, qwe=1))

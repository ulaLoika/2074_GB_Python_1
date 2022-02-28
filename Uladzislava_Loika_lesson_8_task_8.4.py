from functools import wraps

def val_checker(validate):
    def valid (func):
        @wraps(func)
        def wrapper(*args):
            if args:
                for arg in args:
                    if not validate(arg):
                        raise ValueError (f'Введите число! Вы ввели: {arg}')
            return func(*args)
        return wrapper
    return valid

def validate(x):
    if isinstance(x, int) and x >= 0:
        return True
    return False

@val_checker(validate)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('a'))

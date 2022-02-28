from functools import wraps


def type_logger(calc_cube):
    @wraps(calc_cube)
    def wrapper(*args):
        my_list = []
        for i in range(len(args)):
            if i < len(args) - 1:
                my_list.append(f'{calc_cube.__name__}({args[i]}: {type(args[i])})')
            else:
                my_list.append(f'{calc_cube.__name__}({args[i]}: {type(args[i])})')
        return my_list
    return wrapper


@type_logger
def calc_cube(number):
    print (number)
    return number**3


print (', '.join(i for i in calc_cube(5.0, 2.5)))
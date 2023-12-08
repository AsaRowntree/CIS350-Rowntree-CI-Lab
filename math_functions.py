def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b


def absolute_value(a):
    if a >= 0:
        return a
    else:
        return a * -1


def squared(a):
    return a ** 2


if __name__ == '__main__':
    print('Adding:', add_numbers(2, 4))
    print('Subtracting:', subtract_numbers(9, 2))
    print('Multiplying:', multiply_numbers(5, 2))
    print('Dividing:', divide_numbers(12, 4))
    print(absolute_value(-13))
    print(squared(8))

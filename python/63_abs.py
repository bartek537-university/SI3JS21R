import math


def my_abs(number: float) -> float:
    return number if number > 0 else -number


print(my_abs(-3))
print(my_abs(2))
print(my_abs(3.14))
print(my_abs(-1 / math.inf))
print(my_abs(0))

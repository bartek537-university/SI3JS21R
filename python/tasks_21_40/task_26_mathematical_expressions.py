import math


def task_a_plus(alfa: float, beta: float) -> float:
    return 2 * math.sin((alfa + beta) / 2) * math.cos((alfa - beta) / 2)


def task_a_minus(alfa: float, beta: float) -> float:
    return 2 * math.sin((alfa - beta) / 2) * math.cos((alfa + beta) / 2)


def task_b(x: float, n: int) -> float:
    current_word = 1
    binomial_sum = current_word

    for i in range(n):
        current_word *= (n - i) * x / (i + 1)
        binomial_sum += current_word

    return binomial_sum


def task_c(a: float, b: float, c: float) -> float:
    delta = b ** 2 - 4 * a * c
    return (-b - math.sqrt(delta)) / (2 * a)


def task_d(x: float, iterations: int = 100) -> float:
    current_word = 1
    e_sum = current_word

    for i in range(iterations):
        current_word *= x / (i + 1)
        e_sum += current_word

    return e_sum


def task_e(arg_as: list[float], arg_bs: list[float], x: float, l: float, iterations: int = 100) -> float:
    assert len(arg_as) >= iterations and len(arg_bs) >= iterations

    total = arg_as[0]

    for n in range(1, iterations):
        angle = n * math.pi * x / l
        total += arg_as[n] * math.cos(angle) + arg_bs[n] * math.sin(angle)

    return total


print(task_e([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1, 1, 5))

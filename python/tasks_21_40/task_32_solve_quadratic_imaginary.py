from __future__ import annotations

with open("wspolczynniki.txt") as input_file:
    a, b, c = input_file.readlines()
    a, b, c = int(a), int(b), int(c)


def solve_quadratic_equation(a: float, b: float, c: float) -> (
        float | tuple[float, float] | complex | tuple[complex, complex] | None):
    if a == 0 and b == 0:
        if c == 0:
            return c
        else:
            return None

    if a == 0:
        return -c / b

    delta = b ** 2 - 4 * a * c
    delta_sqrt = delta ** (1 / 2)

    first = (-b - delta_sqrt) / (2 * a)
    second = (-b + delta_sqrt) / (2 * a)

    if delta == 0:
        return first
    return first, second


print(solve_quadratic_equation(a, b, c))

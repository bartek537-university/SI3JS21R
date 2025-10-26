from typing import Callable


def gauss_eliminate(coefficient_matrix: list[list[float]], constant_vector: list[float]) -> None:
    if len(coefficient_matrix) < 1:
        return

    assert len(coefficient_matrix) == len(constant_vector)
    assert all(len(coefficient_matrix[0]) == len(row) for row in coefficient_matrix)

    row_count = len(coefficient_matrix)
    column_count = len(coefficient_matrix[0])

    def swap_rows(a: int, b: int):
        coefficient_matrix[a], coefficient_matrix[b] = coefficient_matrix[b], coefficient_matrix[a]
        constant_vector[a], constant_vector[b] = constant_vector[b], constant_vector[a]

    def add_to_row(target: int, source: int, times: float):
        for column in range(column_count):
            coefficient_matrix[target][column] += coefficient_matrix[source][column] * times
        constant_vector[target] += constant_vector[source] * times

    current_column_index = 0
    current_row_index = 0

    for i in range(min(row_count, column_count)):
        max_row_index = max_indexed(coefficient_matrix[current_row_index:],
                                    key=lambda row: abs(row[current_column_index])) + current_row_index

        max_row_coefficient_value = coefficient_matrix[max_row_index][current_column_index]

        if max_row_coefficient_value == 0:
            current_column_index += 1
            continue

        swap_rows(current_row_index, max_row_index)

        for j in range(current_row_index + 1, row_count):
            multiplier = coefficient_matrix[j][current_column_index] / max_row_coefficient_value
            add_to_row(j, current_row_index, -multiplier)

        current_column_index += 1
        current_row_index += 1


def max_indexed[T](arr: list[T], key: Callable[[T], float]) -> int:
    return max(range(len(arr)), key=lambda index: key(arr[index]))


def solve_linear_equations(coefficient_matrix: list[list[float]], constant_vector: list[float]) -> list[float]:
    assert len(coefficient_matrix) == len(constant_vector)
    assert all(len(coefficient_matrix[0]) == len(row) for row in coefficient_matrix)

    coefficients_rank = matrix_get_rank(coefficient_matrix)
    constants_rank = vector_get_rank(constant_vector)

    extended_matrix_rank = max(coefficients_rank, constants_rank)

    if coefficients_rank != extended_matrix_rank:
        raise ValueError("Inconsistent system. rank[A] != rank[A|b]")

    column_count = len(coefficient_matrix[0])
    if column_count > constants_rank:
        raise ValueError("Infinitely many solutions.")

    # Now we know we're working with a square matrix, which is solvable.

    solutions = [0. for _ in range(extended_matrix_rank)]

    for i in range(coefficients_rank - 1, -1, -1):
        solutions[i] = solve_linear_equation(solutions, coefficient_matrix[i], constant_vector[i])

    return solutions


def matrix_get_rank(matrix: list[list[float]]) -> int:
    return sum([int(any(row)) for row in matrix])


def vector_get_rank(values: list[float]) -> int:
    return len(values) - find_leading_nonzero_value_index(values[::-1])


def solve_linear_equation(solutions: list[float], coefficient_row: list[float], constant: float) -> float:
    assert len(solutions) == len(coefficient_row)

    unsolved_index = find_leading_nonzero_value_index(coefficient_row)

    linear_equation_sum = 0
    for i in range(unsolved_index + 1, len(coefficient_row)):
        linear_equation_sum += coefficient_row[i] * solutions[i]

    return (constant - linear_equation_sum) / coefficient_row[unsolved_index]


def find_leading_nonzero_value_index(values: list[float]) -> int:
    for index, value in enumerate(values):
        if value != 0:
            return index
    return -1


a_coefficients = [
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5],
]

a_solutions = [
    2, -1, 4
]

gauss_eliminate(a_coefficients, a_solutions)

print(a_coefficients)
print(a_solutions)

results = solve_linear_equations(a_coefficients, a_solutions)

print(results)

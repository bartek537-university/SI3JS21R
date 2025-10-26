import random
from typing import Final

RANDOM_RANGE_START: Final[float] = 5.5
RANDOM_RANGE_END: Final[float] = 10.3

row_count = int(input("Podaj liczbę wierszy: "))
column_count = int(input("Podaj liczbę kolumn: "))

matrix = [[random.uniform(RANDOM_RANGE_START, RANDOM_RANGE_END) for _ in range(column_count)] for _ in range(row_count)]


def join_to_str[T](values: list[T]) -> str:
    iterable = [str(value) for value in values]
    return ' '.join(iterable)


with open("danewygenerowane.txt", "w+") as file:
    file.writelines(map(lambda row: f"{join_to_str(row)}\n", matrix))

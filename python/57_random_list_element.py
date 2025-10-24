import random
from typing import Final

LIST_SEPARATOR: Final[str] = ", "

file_name = input("Podaj nazwę pliku: ")


def get_random_element(path: str) -> str | None:
    with open(path) as input_file:
        elements = input_file.readline().split(LIST_SEPARATOR)

        random_line_index = random.randrange(0, len(elements))
        return elements[random_line_index]


print(get_random_element(file_name))

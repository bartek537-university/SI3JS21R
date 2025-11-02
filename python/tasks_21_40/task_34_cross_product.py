from typing import Any, Generator

genders = ["Kobieta", "Mężczyzna"]
colors = ["Biały", "Czarny", "Zielony", "Czerwony", "Niebieski", "Żółty", "Szary"]
sizes = ["XXL", "XL", "L", "M", "S", "XS"]


def cross_product(*arrays: list[Any]) -> Generator[list[...]]:
    empty_result = [None for _ in range(len(arrays))]
    return __cross_product(empty_result, 0, *arrays)


def __cross_product(current_result: list[...], array_index: int, *arrays: list[Any]) -> Generator[list[...]]:
    if array_index >= len(arrays):
        yield current_result
        return

    for value in arrays[array_index]:
        current_result[array_index] = value
        yield from __cross_product(current_result, array_index + 1, *arrays)


for index, label in enumerate(cross_product(genders, colors, sizes)):
    with open(f"metki/metka_{index}.txt", "w+") as label_file:
        label_file.write(" ".join(label) + "\n")

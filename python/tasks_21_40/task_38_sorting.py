from typing import Callable

from sorting_algorithms import bubble_sort, insertion_sort, quick_sort

with open("nieposortowane.txt") as input_file:
    unsorted_numbers = [int(line) for line in input_file]

algorithms = [
    (lambda numbers: bubble_sort(numbers), "bąbelkowe"),
    (lambda numbers: insertion_sort(numbers), "przez wstawienie"),
    (lambda numbers: quick_sort(numbers, 0, len(numbers)), "szybkie"),
]


def sorted_with(fn: Callable[[list[...]], None], values: list[...]) -> list[...]:
    values_copy = values[:]
    fn(values_copy)
    return values_copy


for algorithm, name in algorithms:
    sorted_numbers = sorted_with(algorithm, unsorted_numbers)

    with open(f"posortowane_{name}.txt", "w+") as output_file:
        output_file.writelines([f"{number}\n" for number in sorted_numbers])

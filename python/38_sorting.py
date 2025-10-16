from typing import Callable

from sorting_algorithms import bubble_sort, insertion_sort, quick_sort

with open("38_unsorted.txt") as input_file:
    unsorted_numbers = [int(line) for line in input_file]

algorithms = [
    (lambda numbers: bubble_sort(numbers), "bubble_sort"),
    (lambda numbers: insertion_sort(numbers), "insertion_sort"),
    (lambda numbers: quick_sort(numbers, 0, len(numbers)), "quick_sort"),
]


def sorted_with(fn: Callable[[list[...]], None], values: list[...]) -> list[...]:
    values_copy = values[:]
    fn(values_copy)
    return values_copy


for algorithm, name in algorithms:
    sorted_numbers = sorted_with(algorithm, unsorted_numbers)

    with open(f"38_sorted_{name}.txt", "w+") as output_file:
        output_file.writelines([f"{number}\n" for number in sorted_numbers])

def bubble_sort(array: list[...]) -> None:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def insertion_sort(array: list[...]) -> None:
    for i in range(1, len(array)):
        current_value = array[i]
        j = i

        while j >= 1 and array[j - 1] > current_value:
            array[j] = array[j - 1]
            j -= 1

        array[j] = current_value


def quick_sort(array: list[...], start: int, end: int) -> None:
    if end - start < 1:
        return

    pivot_index = end - 1
    pivot_value = array[pivot_index]

    partition_index = start
    for i in range(start, end - 1):
        if array[i] < pivot_value:
            array[i], array[partition_index] = array[partition_index], array[i]
            partition_index += 1

    array[pivot_index], array[partition_index] = array[partition_index], array[pivot_index]

    quick_sort(array, start, partition_index)
    quick_sort(array, partition_index + 1, end)

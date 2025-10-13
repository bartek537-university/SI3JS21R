def calculate_min_max_average(array: list[int]):
    minimum_element = min(array)
    maximum_element = max(array)
    return (minimum_element + maximum_element) / 2


print(calculate_min_max_average([1, 10, 20, 30, 99, 40, 20]))

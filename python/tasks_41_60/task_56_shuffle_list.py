import random


def shuffle(array: list[...]) -> None:
    if len(array) < 2:
        return
    element_count = len(array)
    for current_index in range(element_count):
        random_index = random.randrange(0, element_count)
        array[current_index], array[random_index] = array[random_index], array[current_index]


my_list = [*range(25)]
shuffle(my_list)
print(my_list)

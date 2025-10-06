from statistics import mean, median

numbers: list[int]

with open("16_numbers.txt") as file:
    numbers = [int(number) for number in file.readlines()]

print(f"Suma elementów wynosi {sum(numbers)}.")
print(f"Średnia elementów wynosi {mean(numbers)}.")
print(f"Mediana elementów wynosi {median(numbers)}.")

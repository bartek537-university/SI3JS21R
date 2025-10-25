from statistics import mean, median

number_count = int(input("Podaj ilość liczb: "))
numbers: list[int] = []

for number_index in range(number_count):
    number_value = int(input(f"[{number_index + 1}]: "))
    numbers.append(number_value)

print(f"Suma elementów wynosi {sum(numbers)}.")
print(f"Średnia elementów wynosi {mean(numbers)}.")
print(f"Mediana elementów wynosi {median(numbers)}.")

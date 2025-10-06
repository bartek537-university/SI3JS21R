from statistics import mean, median

numbers: list[int] = []

while True:
    number = int(input("Podaj liczbę: "))
    numbers.append(number)

    if input("Chcesz dodać kolejną liczbę? [T/n] ").lower() == 'n':
        break

print(f"Suma elementów wynosi {sum(numbers)}.")
print(f"Średnia elementów wynosi {mean(numbers)}.")
print(f"Mediana elementów wynosi {median(numbers)}.")

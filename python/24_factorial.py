number = int(input("Podaj liczbę: "))


def factorial(value: int) -> int:
    for factor in range(value - 1, 1, -1):
        value *= factor
    return value

print(f"{number}! = {factorial(number)}")

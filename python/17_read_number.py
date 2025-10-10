def read_integral(message: str) -> int | None:
    read_value = input(message)

    try:
        return int(read_value)
    except ValueError:
        return None


def calculate_square_area(side: int) -> int:
    return side ** 2


square_side = read_integral("Podaj liczbę całkowitą: ")

if square_side is None:
    print("Nie podałeś liczby całkowitej.")
else:
    square_area = calculate_square_area(square_side)
    print(f"Pole kwadratu o zadanym boku wynosi {square_area}.")

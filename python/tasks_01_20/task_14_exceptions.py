def read_number() -> float:
    while True:
        try:
            return float(input("Podaj liczbę: "))
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")


number = read_number()
print(f"Poprawnie odczytano liczbę {number}.")

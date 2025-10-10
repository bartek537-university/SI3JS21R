from typing import Final

COLUMN_COUNT: Final[int] = 5
ROW_COUNT: Final[int] = 7

fill = int(input("Podaj liczbę (wypełnienie tabeli): "))

with open("wynikzadanie.txt", "w+") as file:
    for _ in range(ROW_COUNT):
        file.write(f"{fill} " * COLUMN_COUNT + "\n")

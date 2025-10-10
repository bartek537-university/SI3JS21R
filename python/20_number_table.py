from typing import Final

COLUMN_COUNT: Final[int] = 5
ROW_COUNT: Final[int] = 7

fill = int(input("Podaj liczbę (wypełnienie tabeli): "))

for _ in range(ROW_COUNT):
    print(f"{fill} " * COLUMN_COUNT)

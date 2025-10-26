from io import TextIOWrapper
from typing import Final

output_file_name = input("Podaj nazwę pliku wyjściowego: ")
iterations = int(input("Podaj ilość iteracji: "))
value_delta = int(input("Podaj podstawę iteracji: "))

COLUMN_WIDTH: Final[int] = 5
COLUMN_FILL_CHAR: Final[str] = "*"
HORIZONTAL_SPACER_EMPTY = "   "
HORIZONTAL_SPACER_DASH = " | "


def align_column_center(text: str) -> str:
    return text.center(COLUMN_WIDTH, COLUMN_FILL_CHAR)


def align_column_left(text: str) -> str:
    return text.ljust(COLUMN_WIDTH, " ")


def print_column_headers(writer: TextIOWrapper) -> None:
    nominator_header = align_column_left("liczn.")
    sum_header = align_column_left("suma")
    writer.write(f"{nominator_header} {HORIZONTAL_SPACER_EMPTY} {sum_header}\n")


def print_column_horizontal_line(writer: TextIOWrapper) -> None:
    decoration = "-" * COLUMN_WIDTH
    writer.write(f"{decoration} {HORIZONTAL_SPACER_EMPTY} {decoration}\n")


def print_iteration_table_body(iteration: int, total: int, writer: TextIOWrapper) -> None:
    iteration_text = align_column_center(str(iteration))
    total_text = align_column_center(str(total))

    horizontal_spacer = HORIZONTAL_SPACER_EMPTY if iteration <= 0 else HORIZONTAL_SPACER_DASH
    writer.write(f"{iteration_text} {horizontal_spacer} {total_text}\n")


with open(output_file_name, "w+") as file:
    value_total = 0

    print_column_headers(file)
    for iteration in range(iterations):
        print_iteration_table_body(iteration, value_total, file)

        if iteration == 0:
            print_column_horizontal_line(file)

        value_total += value_delta

from typing import Callable


def try_parse[T](callable: Callable[[], T]) -> T | None:
    try:
        return callable()
    except ValueError:
        return None


def read_recognize_number_type() -> str:
    text = input("Podaj liczbę: ")

    if try_parse(lambda: int(text)) is not None:
        return "To liczba całkowita."
    if try_parse(lambda: float(text)) is not None:
        return "To liczba zmiennoprzecinkowa."
    if try_parse(lambda: complex(text)) is not None:
        return "To liczba urojona."

    return "To nie jest liczba"


print(read_recognize_number_type())

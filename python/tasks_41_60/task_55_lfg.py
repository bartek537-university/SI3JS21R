from typing import Callable


class LaggedFibonacciGenerator:
    def __init__(self, taps: list[int], history: list[int], operation: Callable[[int, int], int]):
        if len(taps) < 2:
            raise ValueError("Taps must include at least two entries.")
        if min(taps) <= 0:
            raise ValueError("Taps mustn't refer to future elements.")
        if len(history) < max(taps):
            raise ValueError("Not enough history entries to match the tap needs.")

        self.__taps = taps.copy()
        self.__history = history.copy()
        self.__operation = operation

    def __get_tap_value(self, index: int) -> int:
        assert 0 <= index < len(self.__taps)
        return self.__history[-self.__taps[index]]

    def __next__(self):
        current_value = self.__get_tap_value(0)

        for tap_index in range(1, len(self.__taps)):
            current_value = self.__operation(current_value, self.__get_tap_value(tap_index))

        self.__history.append(current_value)

        return current_value


lfg = LaggedFibonacciGenerator([3, 7], [8, 6, 7, 5, 3, 0, 9], lambda x, y: (x + y) % 10)

random_numbers = [next(lfg) for i in range(10)]
print(random_numbers)

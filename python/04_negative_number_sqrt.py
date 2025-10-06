from numbers import Complex
from typing import Final

NEGATIVE_NUMBER: Final[int] = -23
ROOT_ORDER = 2

result: Complex = NEGATIVE_NUMBER ** (1 / ROOT_ORDER)
print(f"{result.real} + {result.imag}i")

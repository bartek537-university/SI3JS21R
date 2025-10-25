import math
import random
from typing import Final

ITERATION_COUNT: Final[int] = 1_000_000


def approximate_pi(iterations: int) -> float:
    hit_count = 0

    for _ in range(iterations):
        x, y = random.random(), random.random()
        is_hit = math.sqrt(x ** 2 + y ** 2) <= 1

        if is_hit:
            hit_count += 1

    return 4 * hit_count / iterations


approximated_pi = approximate_pi(iterations=ITERATION_COUNT)
print(f"π wynosi w przybliżeniu {approximated_pi}.")

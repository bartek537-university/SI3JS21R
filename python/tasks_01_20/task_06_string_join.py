import math
from typing import Final

REPEAT_TIMES: Final[int] = 10

print('@'.join([str(-0.7 * math.e + 4.07)] * REPEAT_TIMES))

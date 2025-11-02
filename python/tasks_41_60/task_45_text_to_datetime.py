from datetime import datetime
from typing import Final

ISO_DATE: Final[str] = "2025-06-05T12.192"
WEIRD_DATE: Final[str] = "12:2025-05-192-06"

a = datetime.fromisoformat(ISO_DATE)
print(a)

b = datetime.strptime(WEIRD_DATE, "%H:%Y-%d-%f-%m")
print(b)
import datetime
from datetime import timedelta
from typing import Final

DAYS_IN_WEEK: Final[int] = 7

year_text, week_text = input("in: ").split(", ")


def get_first_week_monday(year: int):
    date = datetime.date(year, 1, 1)

    if date.isocalendar().week != 1:
        # This day counts towards last year's weeks.
        date += timedelta(days=DAYS_IN_WEEK)

    return date - timedelta(days=date.weekday())


first_week_monday = get_first_week_monday(int(year_text))
selected_week_monday = first_week_monday + timedelta(days=DAYS_IN_WEEK * (int(week_text) - 1))

print("out:", selected_week_monday.strftime("%a %b %d %H:%M:%S %Y"))

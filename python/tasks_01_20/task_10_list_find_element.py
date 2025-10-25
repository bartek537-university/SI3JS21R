from typing import Final

from task_07_list_comprehension import result_list as list_a
from task_08_list_print import result_list as list_b

ELEMENT_TO_FIND: Final[object] = "tekst"

a_contains_element = ELEMENT_TO_FIND in list_a
b_contains_element = ELEMENT_TO_FIND in list_b

if ELEMENT_TO_FIND in list_a:
    print(f"Element znajduje się na pierwszej liście {list_a.count(ELEMENT_TO_FIND)} raz(y).")

if ELEMENT_TO_FIND in list_b:
    print(f"Element znajduje się na drugiej liście {list_b.count(ELEMENT_TO_FIND)} raz(y).")

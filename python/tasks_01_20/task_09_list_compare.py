from task_07_list_comprehension import result_list as list_a
from task_08_list_print import result_list as list_b

print(list_a == list_b)
print(list_a[12:14] == list_b[10:12])  # ["tekst", False]
print(list_a[15] == list_b[13])  # 1+2j
print(list_a[-2] == (not list_b[11]))  # True, not False
print(list_a[0] == list_b[-1])  # ["mleko", "jajka", "mąka", "cukier"]

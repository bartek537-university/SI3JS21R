import math

result_list: list[object] = [chr(ordinal) for ordinal in range(ord('A'), ord('Z'), 3)]

result_list.append(math.tan(math.pi / 4))
result_list.append("tekst")
result_list.extend([False, "zielony", 1 + 2j])
result_list.append({"hello": "cześć"})
result_list.append(["mleko", "jajka", "mąka", "cukier"])

if __name__ == "__main__":
    print(result_list[3::-1], result_list[11], result_list[12:], sep="\n")

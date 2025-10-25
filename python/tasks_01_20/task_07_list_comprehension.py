result_list: list[object] = [number ** 2 for number in range(1, 11)]

result_list.append(3.14)
result_list.append("tekst")
result_list.extend([False, "żółty", complex(1 + 2j)])
result_list.append({"hello": "witaj"})
result_list.insert(0, ["mleko", "jajka", "mąka", "cukier"])
result_list.append(True)
result_list.append("tekst")

if __name__ == "__main__":
    print(result_list)

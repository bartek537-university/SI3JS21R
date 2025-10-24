ROMAN_INTEGER_MAPPING = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def roman_to_integer(roman: str) -> int:
    integer_result = 0
    current_sequence = ""

    for letter in roman + "\0":
        new_sequence = current_sequence + letter

        if new_sequence in ROMAN_INTEGER_MAPPING:
            current_sequence = new_sequence
            continue

        integer_result += ROMAN_INTEGER_MAPPING[current_sequence]
        current_sequence = letter

    return integer_result


print(roman_to_integer("MMXXV"))  # 2025
print(roman_to_integer("XXI"))  # 21
print(roman_to_integer("MCMXVIII"))  # 1918
print(roman_to_integer("MMMCMXCIX"))  # 3999
print(roman_to_integer("CDXCIX"))  # 499

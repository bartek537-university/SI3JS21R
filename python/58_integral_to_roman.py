ROMAN_INTEGER_MAPPING = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
]


def integral_to_roman(value: int) -> str:
    roman_result = ""
    roman_index = 0

    while value > 0:
        current_roman_text, current_roman_value = ROMAN_INTEGER_MAPPING[roman_index]
        roman_value_repetitions = value // current_roman_value

        if roman_value_repetitions > 3:
            raise ValueError("The value is too high.")

        value -= current_roman_value * roman_value_repetitions

        roman_result += current_roman_text * roman_value_repetitions
        roman_index += 1

    return roman_result


print(integral_to_roman(2025))  # MMXXV
print(integral_to_roman(21))  # XXI
print(integral_to_roman(1918))  # MCMXVIII
print(integral_to_roman(3999))  # MMMCMXCIX
print(integral_to_roman(499))  # CDX

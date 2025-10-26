import math

entered_number = input()

if "." in entered_number:
    integral_text, decimal_text = entered_number.split(".")
    integral, decimal = int(integral_text), int(decimal_text)

    denominator = 10 ** len(decimal_text)
    nominator = decimal + integral * denominator

    fraction_gcd = math.gcd(nominator, denominator)

    denominator //= fraction_gcd
    nominator //= fraction_gcd

    print(f"{nominator}/{denominator}")

from typing import Final

VOWELS: Final[str] = "aeiouy"

input_text = input("Podaj dowolny tekst: ")

for vowel in VOWELS:
    occurrence_count = input_text.count(vowel)

    if occurrence_count > 0:
        print(f"{vowel} występuje {occurrence_count} razy")

from typing import Final

VOWELS: Final[str] = "aeiouyąęó"

text_to_analyze = input("Podaj tekst: ")

vowel_count = 0
for letter in text_to_analyze:
    if letter in VOWELS:
        vowel_count += 1

print(f"Liczba samogłosek: {vowel_count}")

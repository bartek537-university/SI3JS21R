def is_palindrome(text_to_check: str) -> bool:
    return text_to_check == text_to_check[::-1]


text = input("Podaj tekst do sprawdzenia: ")
print(f"Podany tekst {"jest" if is_palindrome(text) else "nie jest"} palindromem")

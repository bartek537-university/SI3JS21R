letters_to_count_text = input("Podaj litery do przeliczenia: ")
letters_to_count = {*letters_to_count_text}

with open("tekstwejsciowy.txt") as file:
    file_str = '\s'.join(file.readlines())

for letter in letters_to_count:
    print(f"Litera {letter} występuje {file_str.count(letter)} razy.")

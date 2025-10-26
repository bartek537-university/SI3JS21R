letters_to_count_text = input("Podaj litery do przeliczenia (jedna po drugiej, bez spacji): ")
letters_to_count = {*letters_to_count_text}

with open("tekstwejsciowy.txt") as file:
    file_str = ''.join(file.readlines())

for letter in letters_to_count:
    print(f"Litera {letter} występuje {file_str.count(letter)} razy.")

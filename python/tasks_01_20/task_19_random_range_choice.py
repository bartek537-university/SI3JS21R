import random

a = int(input("Podaj początek przedziału: "))
b = int(input("Podaj koniec przedziału: "))

random_number = random.randint(a, b)

file_name = input("Podaj nazwę pliku: ")

with open(file_name) as input_file:
    file_contents = input_file.readlines()

random_element = random.choice(file_contents)

with open("wynikzadanie.txt", 'w+') as output_file:
    output_file.write(f"{random_number}\n")
    output_file.write(f"{random_element}\n")

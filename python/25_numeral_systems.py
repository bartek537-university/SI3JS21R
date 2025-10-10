with open("danezadanie.txt") as input_file:
    number = int(input_file.readline())

hexadecimal = hex(number)
octal = oct(number)

with open("liczbykonwertowane.txt", "w+") as output_file:
    values_to_write = [number, hexadecimal, octal]
    output_file.writelines([f"{value}\n" for value in values_to_write])

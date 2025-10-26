input_file = open("tekstdostatystyki.txt")
output_file = open("wersaliki.txt", "w+")

for line in input_file:
    output_file.write(line.upper())

output_file.close()
input_file.close()

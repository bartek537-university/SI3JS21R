element_count = int(input("Podaj ilość elementów: "))
elements = []

for element_index in range(element_count):
    element_value = input(f"[{element_index + 1}]: ")
    elements.append(element_value)

print('\n'.join(elements))

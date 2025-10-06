entered_elements = []

while True:
    element = input("Podaj wartość kolejnego elementu listy: ")
    entered_elements.append(element)

    if input("Chcesz dodać kolejny element? [T/n] ").lower() == 'n':
        break

print('\n'.join(entered_elements))

start_year = int(input("Podaj rok początkowy: "))
end_year = int(input("Podaj rok końcowy: "))

# Instead of iterating over each year, we find the nearest multiple of 4
# for the start year and increment year counter by 4.
start_year_next_multiple = (start_year + 3) // 4 * 4

for year in range(start_year_next_multiple, end_year + 1, 4):
    if year % 100 == 0 and year % 400 != 0:
        continue
    print(year)

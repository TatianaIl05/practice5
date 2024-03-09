year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0:
    print(366)
else:
    print(365)

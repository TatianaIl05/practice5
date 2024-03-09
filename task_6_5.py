day_1, day_2, day_3 = map(int, input('Введите количество человек: ').split())
i = 1
if day_1 == day_2:
    i += 1
if day_1 == day_3:
    i += 1
if day_2 == day_3:
    if day_1 != day_2:
        i += 1
print(i)

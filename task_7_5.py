n, k, m = map(int, input('Введите количество станций, станцию Артёма и нужную станцию: ').split())
count_clockwise = abs(m - k) - 1
count_counter = n - max(k, m) + min(k, m) - 1
if n < k or n < m:
    print('Ошибка')
elif k == m:
    print(0)
elif count_clockwise >= count_counter:
    print(count_counter)
else:
    print(count_clockwise)

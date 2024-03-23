pin_code = input('Введите PIN-код: ')
answer = 'OK'

if len(pin_code) != 4:
    answer = 'ERROR'

for number in pin_code:
    if pin_code.count(number) > 1:
        answer = 'ERROR'

if 1900 <= int(pin_code) <= 2050:
    answer = 'ERROR'

print(answer)

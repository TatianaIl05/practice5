pin_code = int(input('Введите PIN-код: '))
answer = 'OK'
if 1900 <= pin_code <= 2050:
    answer = 'ERROR'
if len(str(pin_code)) != 4:
    answer = 'ERROR'
if len(str(pin_code)) != len(set(str(pin_code))):
    answer = 'ERROR'
print(answer)

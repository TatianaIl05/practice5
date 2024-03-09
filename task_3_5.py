number = int(input('Введите число: '))
if number % 10 == number//1000:
    if (number - number % 10 - 1000*(number//1000)) % 110 == 0:
        print('настоящее')
    else:
        print('кривое')
else:
    print('кривое')

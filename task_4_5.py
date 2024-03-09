number_of_parrots = int(input('Введите количество попугаев: '))
match number_of_parrots % 10:
    case 1:
        print(number_of_parrots, 'попугай')
    case 2 | 3 | 4:
        print(number_of_parrots, 'попугая')
    case 5 | 6 | 7 | 8 | 9 | 0:
        print(number_of_parrots, 'попугаев')

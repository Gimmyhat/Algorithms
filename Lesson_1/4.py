# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from random import randint, uniform

while True:
    dict_func = {
        '1': [int, '1. случайное целое число'],
        '2': [float, '2. случайное вещественное число'],
        '3': [ord, '3. случайный символ']
    }

    ch_str = '\n'.join(v[1] for v in dict_func.values())
    user_choice = input(f'Выбирай, что будем генерить (укажи цифру)\n{ch_str}\n')
    u_range = list(map(dict_func[user_choice][0], input('Введи границы диапазона: ').split()))
    u_range.sort()

    if user_choice == '1':
        print(randint(*u_range))
    elif user_choice == '2':
        print(uniform(*u_range))
    else:
        print(chr(randint(*u_range)))

    if input('Продолжаем?.. (y/n)') == 'n':
        break

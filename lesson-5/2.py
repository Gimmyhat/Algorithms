# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом
# каждое число представляется как массив, элементы которого это цифры числа. Например,
# пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# вариант попроще
# num1 = input('Введите 1-е число: ')
# num2 = input('Введите 2-е число: ')
# print(hex(int(num1, 16) + int(num2, 16))[2:])
# print(hex(int(num1, 16) * int(num2, 16))[2:])

from collections import deque


def hex_to_int(num16: list):
    f = '0123456789ABCDEF'
    return sum(f.find(n.upper()) * 16 ** (len(num16) - i - 1) for i, n in enumerate(num16))


def int_to_hex(n: int):
    f = '0123456789ABCDEF'
    num16 = deque()
    while n:
        num16.appendleft(f[n % 16])
        n //= 16
    return list(num16)


a = hex_to_int(list(input('Введите 1-е число: ')))
b = hex_to_int(list(input('Введите 2-е число: ')))

print(int_to_hex(a + b), int_to_hex(a * b))

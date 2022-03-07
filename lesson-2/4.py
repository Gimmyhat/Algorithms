# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов
# (n) вводится с клавиатуры.

def sum_elements(x, count):
    return sum_elements(x / -2, count - 1) + x if count > 1 else x


print(sum_elements(1, int(input('Введите количество элементов: '))))

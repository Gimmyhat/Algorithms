# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = input('Введите число: ')
even = len([i for i in n if int(i) % 2 == 0])
odd = len(n) - even
print(f'В числе {n} четных цифр: {even}, нечетных: {odd}')

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

num_list = tuple(map(int, input('Введите числа через пробел: ').split()))
res_list = tuple(sum(int(n) for n in str(num)) for num in num_list)
idx = res_list.index(max(res_list))
print(f'Результат: число {num_list[idx]}, сумма цифр {res_list[idx]}')

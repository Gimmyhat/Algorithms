# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from math import prod

n = int(input('Введите число: '))
nums = list(map(int, str(n)))
print(f'Сумма цифр числа = {sum(nums)}\nпроизведение цифр числа = {prod(nums)}')

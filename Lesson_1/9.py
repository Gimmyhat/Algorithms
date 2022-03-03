# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

arr3 = sorted(list(map(int, input('Введи 3 разных числа: ').split())))
print('Среднее:', arr3[1])

# arr3 = set(map(int, input('Введи 3 разных числа: ').split()))
# print('Среднее:', *arr3.difference({max(arr3), min(arr3)}))

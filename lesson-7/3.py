# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
# равные части: в одной находятся элементы, которые не меньше медианы, в другой –
# не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это
# слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


def my_median(lst):
    i = 1
    while i <= m:
        lst.remove(max(lst))
        i += 1
    return max(lst)


if __name__ == '__main__':
    # Решение без сортировки исходного массива
    m = int(input('Введите число: '))
    lst_obj = [random.randint(0, 100) for _ in range(0, 2 * m + 1)]

    print(lst_obj)
    print(my_median(lst_obj[:]))

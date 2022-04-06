# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции. По
# возможности доработайте алгоритм (сделайте его умнее).

from random import randrange
from timeit import timeit


def bubble_sort(a):
    n = 1
    while n < len(a):
        for i in range(len(a) - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n += 1
    return a


def hairbrush_sort(a):
    f = 1.247  # Фактор уменьшения рассчитан опытным и теоретическим путем
    step = int(len(a) / f)
    while step >= 1:
        i = 0
        while i + step < len(a):
            if a[i] > a[i + step]:
                a[i], a[i + step] = a[i + step], a[i]
            i += 1
        step = int(step / f)
    return a


if __name__ == '__main__':
    arr = [randrange(-100, 100) for _ in range(100)]

    print(arr)
    print(bubble_sort(arr[:]))
    print(hairbrush_sort(arr[:]))

    print(timeit('bubble_sort(arr[:])', globals=globals(), number=10000))  # 13.273048900067806
    print(timeit('hairbrush_sort(arr[:])', globals=globals(), number=10000))  # 3.7485317999962717

# В «пузырьке» при переборе массива сравниваются соседние элементы.
# Основная идея «расчёски» в том, чтобы первоначально брать достаточно большое расстояние между
# сравниваемыми элементами и по мере упорядочивания массива сужать это расстояние вплоть до минимального.
#
# Эффективность сортировки расческой по сравнению с методом пузырька растет с увеличением размера массива.

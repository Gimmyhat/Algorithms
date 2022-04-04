# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же
# задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и
# разрядность вашей ОС.

# Python 3.10 Windows 64

from memory_profiler import memory_usage
from timeit import default_timer
from pympler import asizeof
from collections import namedtuple


def check(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - t1
        print(f'{res}, {mem_diff}, {time_diff}')

    return wrapper


# Скрипт №1
# Неоптимизированное решение

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker = Position('Ivan', 'Ivanov', 'Boss', 500, 50)
print(asizeof.asizeof(worker))  # 960


# Оптимизированное
class Worker:
    __slots__ = ['name', 'surname', 'position', 'wage', 'bonus']

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        income = namedtuple('income', 'wage bonus')
        self._income = income(
            wage=wage,
            bonus=bonus
        )


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income.wage + self._income.bonus)


worker = Position('Ivan', 'Ivanov', 'Boss', 500, 50)
print(asizeof.asizeof(worker))  # 536


# Благодаря использованию слотов, а также замене словаря на именованный кортеж размер
# экземпляра класса уменьшился правктически в 2 раза


# Скрипт №2
# Неопмизированное
@check
def not_optimized():
    def sum_num_list(number):
        result = 0
        num_list = list(str(number))
        for numb in num_list:
            result += int(numb)
        return result

    my_list = []
    for num in range(0, 10000):
        if num % 2:
            my_list.append(num ** 3)

    summary = 0
    for num in my_list:
        if not sum_num_list(num) % 7:
            summary += num
    print(summary)

    for idx in range(0, len(my_list)):
        my_list[idx] += 17

    summary = 0
    for num in my_list:
        if not sum_num_list(num) % 7:
            summary += num
    print(summary)


not_optimized()  # mem_diff = 0.265625, time_diff = 0.149514798


# Оптимизированное

@check
def optimized():
    def sum_num_list(number):
        summary = 0
        num_list = list(str(number))
        for numb in num_list:
            summary += int(numb)
        return summary

    my_list = [num ** 3 for num in range(10000) if num % 2]

    gen_obj = (num for num in my_list if not sum_num_list(num) % 7)
    print(sum(gen_obj))

    for idx in range(0, len(my_list)):
        my_list[idx] += 17
    gen_obj = (num for num in my_list if not sum_num_list(num) % 7)
    print(sum(gen_obj))


optimized()  # mem_diff = 0.02734375, time_diff = 0.13852836200000007


# Оптимизированная функция имеет значительный выигрыш по памяти
# за счет использования генераторов и lc


# Скрипт №3
# Неоптимизированный
@check
def reform(lst):
    for price in lst:
        rub = int(price)
        penny = int((price - int(price)) * 100)
        print(f'{rub:02d} руб {penny:02d} коп', end=', ')
    print('')


prices = [46.7, 97.2, 34.84, 54, 779.52, 21.09, 13.3, 9.8, 55.06, 88.8]
reform(prices)  # mem_diff = 0.00390625, time_diff = 0.10465618500000007


# Оптимизированный
@check
def reform(lst):
    res = (f'{int(price):02d} руб {int((price - int(price)) * 100):02d} коп '
           for price in lst)
    print(*res)


prices = [46.7, 97.2, 34.84, 54, 779.52, 21.09, 13.3, 9.8, 55.06, 88.8]
reform(prices) # mem_diff = 0,0 time_diff = 0.10492150099999997
# Оптимизированная функция имеет выигрыш по памяти за счет использования генератора
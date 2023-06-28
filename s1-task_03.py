"""
Задача No3. Решение в группах
В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.

Выведите наименьшее число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32
"""
import math

students_a = 20
students_b = 21
students_c = 22


def tables_in_one_class(students_class):
    tables = math.ceil(students_class / 2)
    return tables


count_tables = tables_in_one_class(students_a) + tables_in_one_class(students_b) + tables_in_one_class(students_c)

print(count_tables)

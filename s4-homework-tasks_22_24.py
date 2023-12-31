from random import randint

# Урок 4. Словари, множества и профилирование

"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).

Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""
# ---------------------------------------------------------------- 22

n = int(input("Введите количество элементов первого набора чисел: "))
m = int(input("Введите количество элементов второго набора чисел: "))

lst1 = []
for _ in range(n):
    lst1.append(int(input("Введите элемент первого набора чисел: ")))

lst2 = []
for _ in range(m):
    lst2.append(int(input("Введите элемент второго набора чисел: ")))

print(lst1, lst2)

a = set(lst1)
b = set(lst2)

c = sorted(a.intersection(b))

print(c)
# =============================================================== END


"""
Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
# ---------------------------------------------------------------- 24


bushes = int(input('Введите количество кустов черники: '))
berries = []
for _ in range(bushes):
    a = randint(0, 20)
    berries.append(a)
print(f"Количество ягод на кустах: {berries}")

collect = [berries[0] + berries[-1] + berries[-2]]
for i in range(len(berries) - 1):
    collect.append(berries[i] + berries[i - 1] + berries[i + 1])
print(f"Макисимальное количество ягод на соседних кустах: {max(collect)}")

# =============================================================== END

# Урок 1. Ввод-Вывод, операторы ветвления

"""Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
# ---------------------------------------------------------------- 2

n = int(input('Enter 3-digit number: '))
if 100 < n <= 999:
    n1 = n // 100
    n2 = n // 10 % 10
    n3 = n % 10
else:
    print('Invalid number')

print(n1 + n2 + n3)

# ============================================================== END

"""
Задача 4:
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""
# ---------------------------------------------------------------- 4

s = int(input("Input count of birds (multiple of 4): "))

if s % 4 != 0:
    print("Try again. Enter a multiple of 4.")
else:
    peter = int(s / 4)
    serge = int(s / 4)
    kate = int(s / 2)

print(f'Peter: {peter}, Serge: {serge}, Kate: {kate}')

# ============================================================== END

"""
Задача 6:
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no
"""

# ---------------------------------------------------------------- 6

number_of_ticket = input("Input number of ticket (6-digit): ")

if len(number_of_ticket) != 6:
    print("Enter a valid number.")
elif int(number_of_ticket[0]) \
        + int(number_of_ticket[1]) \
        + int(number_of_ticket[2]) \
        == int(number_of_ticket[-1]) \
        + int(number_of_ticket[-2]) \
        + int(number_of_ticket[-3]):
    print("Lucky!")
else:
    print("Don't worry, better luck next time.")

# ============================================================== END

"""
Задача 8:
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

# ---------------------------------------------------------------- 8

n = int(input("Enter the number of slices along the length of the chocolate bar: "))
m = int(input("Enter the number of slices along the width of the chocolate bar: "))
k = int(input("Enter the number of slices to be broken off: "))

x = m * n

if k > x:
    print(
        f"The number of slices to be broken off cannot be more than the number of slices in chocolate. "
        f"Please enter no more than {x} pieces. Please try again.")
elif k % m == 0 or k % n == 0:
    print("Yes")
else:
    print("No")

# ============================================================== END

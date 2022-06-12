# Hometask_13_1 Из полученного списка чисел создайте список с суммами этих чисел,
# отсортированными по возрастанию


# def summa(lst):
#     lst1 = []
#     for i in lst:
#         sm = 0
#         while i != 0:
#             j = i % 10
#             sm += j
#             i = i // 10
#         lst1.append(sm)
#     return sorted(lst1)


# print(summa(int(i) for i in input().split()))

# Hometask_13_2 Напишите функцию f(x), которая возвращает значение следующей
# функции, определённой на всей числовой прямой:

# def f(x):
#     if x <= -2:
#         y = 1 - (x + 2)**2
#     elif -2 < x <= 2:
#         y = - x / 2
#     elif x > 2:
#         y = (x - 2)**2 + 1
#     return y
#
#
# print(f(float(input())))

# Hometask_13_3 Напишите функцию, которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два


# def func(lst):
#     lst1 = []
#     for i in lst:
#         if i % 2 == 0:
#             j = i / 2
#             lst1.append(j)
#     return lst1
#
#
# print(func(int(i) for i in input().split()))

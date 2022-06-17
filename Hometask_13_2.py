import random


# 13_4 Напишите функцию, которая создает список случайных элементов.
# На вход функция принимает кол-во элементов, минимальное и максимальное значение

# ax = int(input('enter quantity: '))
# bx = int(input('enter min number: '))
# cx = int(input('enter max number: '))
# lst = []
#
# def rand_nums(a, b, c):
#     for i in range(1, ax + 1):
#         i = random.randint(bx, cx)
#         lst.append(i)
#     return lst
# print(rand_nums(ax, bx, cx))

# 13_5 Преобразуйте задачу с покупкой торта из экзамена 2 в функцию.

# d = {"наполеон": [["масло", "мука", "сахар"], 5, 700],
#      "медовик": [["масло1", "мука1", "сахар1"], 6, 800],
#      "киевский": [["масло2", "мука2", "сахар2"], 7, 900]}
# client_wants1 = input("Какой торт Вы хотели бы приобрести: ").lower()
# what_ask1 = input("Что Вы хотели бы уточнить: ").lower()
#
#
# def pizza(client_wants, what_ask):
#     if what_ask == 'описание':
#         return f"Торт {client_wants} состоит из {d[client_wants][0]}"
#     elif what_ask == 'цена':
#         return f"Торт {client_wants} стоит {d[client_wants][1]} рубля(ей)"
#     elif what_ask == 'количество':
#         return f"Торт {client_wants} осталось {d[client_wants][2]} грамм)"
#
# print(pizza(client_wants1, what_ask1))
#
# how1 = int(input('сколько торта Вам положить: '))
#
# def pizza1(client_wants, what_ask, how):
#     return f'к оплате {int ( d[client_wants][1] ) * how / 100}, торта {client_wants} осталось {d[client_wants][2] - how} грамм'
#
# print(pizza1(client_wants1, what_ask1, how1))

# 13_6 Напишите функцию, вычисляющую значение факториала числа N. Используйте рекурсию


# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x-1) * x
#
# print(fact(int(input('enter: '))))

# 2_1 Дан список чисел.
# Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.

# lst = input("enter numbers: ").split()
# for i in lst:
#     if lst.count(i) == 1:
#         print(i)

# 2_2 Дан список символов. Посчитайте сколько в нем пар элементов,
# равных друг другу (одинаковых).
# Считается, что любые два элемента, равные друг другу, образуют одну пару,
# которую необходимо посчитать.

# lst = input('enter numbers: ').split()
# t = set(lst)
# print(t)
# print(len(lst) - len(t))

# 2_3 Даны 2 кортежа:
# c_1 = (35, 78,21,37, 2,98, 6, 100, 231) c_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1. Сумма элементов какого из
# кортежей больше
# 2. Порядковые номера
# минимальных и максимальных элементов этих кортежей.

# c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
# if sum(c_1) > sum(c_2):
#     print(f'Сумма больше в кортеже {c_1}')
# else:
#     print(f'Сумма больше в кортеже {c_2}')
# print(f'В кортеже с_1 минимальный элемент {c_1.index(min(c_1))}, максимальный элемент {c_1.index(max(c_1))}')
# print(f'В кортеже с_2 минимальный элемент {c_2.index(min(c_2))}, максимальный элемент {c_2.index(max(c_2))}')

# 2_4 Дана строка: ' An apple a day keeps the doctor away'
# Создайте из нее словарь: ключи – элементы строки, значения – количество вхождений данного
# элемента в строку.

# str1 = (' An apple a day keeps the doctor away')
# d = {i: str1.count(i) for i in str1}
# print(d)

# 2_5 Клиент приходит в кондитерскую. Реализуйте кондитерскую:
# 1. Если клиент хочет посмотреть
# описание – название и состав
# 2. Цену – название и стоимость
# 3. Количество – название и
# сколько осталось.
# 4. Купить – стоимость покупки и
# остаток в кондитерской.
# Словарь: ключи – название продукции, значения – описание, стоимость, количество.

# d = {"наполеон": [["масло", "мука", "сахар"], 5, 700],
#      "медовик": [["масло1", "мука1", "сахар1"], 6, 800],
#      "киевский": [["масло2", "мука2", "сахар2"], 7, 900]}
# client_wants = input("Какой торт Вы хотели бы приобрести: ").lower()
# what_ask = input("Что Вы хотели бы уточнить: ").lower()
# if what_ask == 'описание':
#     print(f"Торт {client_wants} состоит из {d[client_wants][0]}")
# elif what_ask == 'цена':
#     print(f"Торт {client_wants} стоит {d[client_wants][1]} рубля(ей)")
# elif what_ask == 'количество':
#     print(f"Торт {client_wants} осталось {d[client_wants][2]} грамм)")
#
# how = int(input('сколько торта Вам положить: '))
# print(f'к оплате {int(d[client_wants][1]) * how / 100}, торта {client_wants} осталось {d[client_wants][2] - how} грамм')

# 2_6 Даны 2 списка чисел. В них могут быть одинаковые числа.
# Посчитайте, сколько в списках одинаковых чисел.

# numb1 = set(int(i) for i in input('enter number1: ').split())
# numb2 = set(int(i) for i in input('enter number2: ').split())
# iter = 0
# for i in numb1:
#     if i in numb2:
#         iter += 1
# print(iter)

# 2_7 Напишите программу, демонстрирующую работу try\except\finally.

# d = {'AI92': 2, 'AI95': 3}
# try:
#     typex = input('enter марка топлива (AI92, AI95): ').upper()
#     number = int(input('enter количество: '))
#     print(f'С Вас {number * d[typex]} рублей')
# except ValueError:
#     print('Введите количество в цифрах')
# except KeyError:
#     print(f'Есть только {[key for key in d]}, выберите из них')
# finally:
#     print('Приезжайте к нам еще')

# 2_8 В текстовый файл построчно записаны фамилия, имя учащихся класса
# и его оценка за тест. Вывести на экран всех учащихся,
# чья оценка меньше 3 баллов и посчитать средний балл по классу.
# iter = 0
# sum1 = 0
# with open('text.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip('\n')
#         iter += 1
#         sum1 += int(line[-1])
#         if int(line[-1]) < 3:
#             print(line)
# print(f'Средняя оценка за тест = {sum1 / iter}')

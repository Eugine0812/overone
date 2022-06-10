# import random


# exam 1_1 с клавиатуры вводится семизначное число.
# Посчитать сколько четных цифр и нечетных.
# num = int(input('enter number'))
# even = 0
# odd = 0
# while num != 0:
#     cur = num % 10
#     if cur % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     num = num // 10
# print('четное=', even, 'нечетное=', odd)

# exam_1_2 С клавиатуры вводится семизначное число.
# Найти сумму его цифр.
# x = int(input('inter number'))
# total = 0
# while x != 0:
#     cur = x % 10
#     total += cur
#     x = x // 10
# print(total)

# exam_1_3 С клавиатуры вводится семизначное число.
# Найти произведение его 1,2 и 5 цифр
# через str
# x = input('enter number')
# y = int(x[0]) * int(x[1]) * int(x[4])
# print(y)

#  через цикл
num = int(input('enter number'))
mult = 1
iter = 1
while num != 0:
    last = num % 10
    if iter == 2 or iter == 5 or iter == 7:
        mult *= last
    num = num // 10
    iter += 1
print(mult)

# exam _2_1 С клавиатуры вводится строка. Посчитаться в ней
# количество гласных букв.
# text = input('enter').lower()
# vowels = ['a', 'e', 'i', 'o', 'y']
# vows = 0
# for i in text:
#     if i in vowels:
#         vows += 1
# print(vows)

# exam_2_2 С клавиатуры вводится строка. Вывести на
# экран все гласные буквы (построчно или в одну строку
# # значения не имеет)
# text = input('enter: ').lower()
# vowels = ['a', 'e', 'i', 'o', 'y']
# for i in text:
#     if i in vowels:
#         print(i, end=' ')

# exam_3_1 Генерируются 2 рандомных числа (a, b) от 1 до 20.
# Сравнить их 9 раз и посчитать сколько раз a > b и наоборот,
# b > a
# a_more_b = 0
# b_more_a = 0
# iter = 1
# while iter <= 9:
#     a = random.randint(1, 20)
#     b = random.randrange(1, 21)
#     print(a, b)
#     if a > b:
#         a_more_b += 1
#     elif a < b:
#         b_more_a += 1
#     iter += 1
# print('a > b: ', a_more_b, 'a < b: ', b_more_a)

# exam_3_2 Сравнить вводимое пользователем число от 1 до 20 N раз
# с рандомным числом от 1 до 20.Каждый раз,
# когда рандомное число больше, выводить на экран
# номер данной итерации.
# num = int(input('enter: '))
# c = int(input('now much'))
# iter = 1
# while iter <= c:
#     r = random.randint(1, 20)
#     print('random: ', r)
#     if r > num:
#         print(f'рандомное число больше в итерации {iter}')
#     iter += 1

# exam_4_1 посчитать сколько раз встречается определенная
# цифра в числаx. Количество введенных чисел,
# искомая цифра и числа, в которых может встречаться
# искомая цифра, задаются с клавиатуры.

# goal = int(input('какую цифру будем искать:'))
# c = int(input('Сколько раз будем искать эту цифру:'))
# count = 0
# iter = 1
# while iter <= 1:
#     num = int(input('введите число: '))
#     while num != 0:
#         last = num % 10
#         if last == goal:
#             count += 1
#         num = num // 10
#     iter += 1
# print(count)

# exam_5_1 С клавиатуры вводится строка, содержащая буквы,
# числа, символы, пробелы. Если в строке математические
# знаки, то вывести их на экран.

# text = input('str: ')
# acts = ['-', '*', '/', '+', '=']
# screen = []
# iter = 0
# for i in text:
#     if i in acts:
#         screen.append(i)
#         iter += 1
# print(iter)
# print(screen)

# exam_6_1 С клавиатуры вводится строка, содержащая буквы,
# числа, символы, пробелы. Посчитать сколько пар букв
# нижнего регистра стоит рядом во введенной строке.

# text = input()
# pair_down = 0
# for i in range(1, len(text)):
#     if text[i-1].islower() and text[i].islower():
#         pair_down += 1
# print(pair_down)

# exam_6_2 С клавиатуры вводится строка,
# содержащая буквы, числа, символы, пробелы.
# Посчитать сколько в строке согласных букв.

# text = input().lower()
# lowels = 'aeioy'
# cons = 0
# for i in range(len(text)):
#     if text[i].isalpha() and text[i] not in lowels:
#         cons += 1
# print(f'В строке {cons} согласных')

#
# for i in range(1, 10):
#     i -= 5
# print(i)


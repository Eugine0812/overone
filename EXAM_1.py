import random


# exam_1_1 С клавиатуры вводится 7мизначное число.
# Если четных цифр в нем больше, чем нечетных, то найти сумму
# всех цифр. Если нечетных больше, чем четных, то найти
# произведение 1, 3 и 6 цифр.
# num = int(input('enter number: '))
# even, odd, summ = 0, 0, 0
# mult, iter = 1, 1
# while num != 0:
#     last = num % 10
#     summ += last
#     if last % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     if iter == 2 or iter == 5 or iter == 7:
#         mult *= last
#     num = num // 10
#     iter += 1
# print('четное=', even, 'нечетное=', odd)
# if even > odd:
#     print(f' четных цифр больше, сумма числа = {summ}')
# elif odd > even:
#     print(f' нечетных цифр больше, произведение числа = {mult}')

# exam_1_2
# С клавиатуры вводится строка. Если количество согласных
# и гласных в ней одинаково, то выведите на экран все
# гласные буквы

# text = input('enter: ').lower()
# vowels = 'aeioy'
# vow, cons = 0, 0
# screen = []
# for i in text:
#     if i.isalpha() and i in vowels:
#         screen.append(i)
#         vow += 1
#     if i.isalpha() and i not in vowels:
#         cons += 1
# if vow == cons:
#     print(screen)
# else:
#     print('end')

# exam_1_3 С клавиатуры вводятся 2 числа a и b и
# генеруется 2 числа рандомно r1 и r2.
# Все числа от 1 до 20.
# Посчитать сколько раз a > r1 and b > r2.
# Проверку выполнить 6 раз.
# В случае равенства (когда a, b больше 3 раза и r1,
# r2 больше 3 раза) вывести на печать рандомные числа,
# полученные в 4 итерации.

# ab_more_r = 0
# r_more_ab = 0
# iter = 1
# str1 = []
# while iter <= 6:
#     num_a = int(input('enter number from 1 till 20: '))
#     num_b = int(input('enter number from 1 till 20: '))
#     r1 = random.randint(1, 20)
#     r2 = random.randint(1, 20)
#     print(num_a, r1, num_b, r2)
#     if num_a > r1 and num_b > r2:
#         ab_more_r += 1
#     if num_b < r1 and num_b < r2:
#         r_more_ab += 1
#     iter += 1
#     if iter == 4:
#         ir1 = r1
#         ir2 = r2
#         str1.append(r1)
#         str1.append(r2)
#     print(ab_more_r, r_more_ab)
#
# if r_more_ab == ab_more_r:
#     print(f"рандомное число в 4ой итерации: {ir1, ir2}")

# exam_1_4 Посчитать сколько раз встречается искомая
# цифра в рандомных числах от 1 до 20. Количество рандомных
# чисел и искомая цифра задаются с клавиатуры.

# num = int(input('what search: '))
# how = int(input('how long search: '))
# count = 0
# iter = 1
# while iter <= how:
#     r = random.randint(1, 20)
#     print(r)
#     while r != 0:
#         last = r % 10
#         if last == num:
#             count += 1
#         r = r // 10
#     iter += 1
# print(f"{num} встречается {count} раз")

# exam_1_5 Вводится строка, содержащая буквы, цифры,
# пробелы и прочие символы. Выведите на печать все цифры.
# Гарантируется, что цифры будут только положительные.

# text = (input('enter str: '))
# nums = "1234567890"
# for i in text:
#     # if i in nums:
#     if i.isdigit():
#         print(i)

# exam_1_6 Вводится строка, содержащая буквы,
# цифры, пробелы и прочие символы.
# Посчитайте:
# - Сколько пар букв (стоят рядом) верхнего регистра
# - Сколько пар букв (стоят
# рядом) нижнего регистра
# - Сколько согласных букв
# - Сколько гласных букв
# - Сколько всего букв
#
# text = input('enter str: ')
# lowels = 'aeioyu'
# low = 0
# con = 0
# pair_up = 0
# pair_down = 0
# iter = 0
# for i in range(1, len(text)):
#     if text[i - 1].islower() and text[i].islower():
#         pair_down += 1
#     elif text[i - 1].isupper() and text[i].isupper():
#         pair_up += 1
# text2 = text.lower()
# for i in range(len(text2)):
#     if i.isalpha() and i in lowels:
#         low += 1
#     elif i.isalpha() and i not in lowels:
#         con += 1
# for i in range(len(text2)):
#     if text[i].isalpha():
#         iter += 1
# print(f ' рядом стоят {pair_up} пар букв верхнего регистра')
# print(f ' рядом стоят {pair_down} пар букв нижнего регистра')
# print(f ' всего гласных: {low}')
# print(f ' всего согласных: {con}')
# print(f ' всего букв: {iter})

# text = input()
# vowels = "eyuoia"
# pair_up, pair_down, cons, vows = 0, 0, 0, 0
# for i in range(1, len(text)):
#     if text[i-1].islower() and text[i].islower():
#         pair_down += 1
#     elif text[i-1].isupper() and text[i].isupper():
#         pair_up += 1
#
#     if text[i - 1].isalpha():
#         if text[i-1].lower() in vowels:
#             vows += 1
#         else:
#             cons += 1
# print(f'''Пар верхнего регистра: {pair_up}
# Пар нижнего регистра: {pair_down}
# гласных букв {vows}
# согласных букв {cons}
# всего букв {vows + cons}''')


# так делать нельзя!!!
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in nums:
#     nums.remove(i)
# print(nums)

# ls = ["ab", "cd"]
# for i in ls:
#     ls.append('x')
# print(ls)

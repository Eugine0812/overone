# 14_1 Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
# Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы
# объекта и вывести на экран все его атрибуты.

# class Dog:
#
#     # создаем атрибуты
#     def __init__(self, height, weight, name, age):
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     # создаем методы
#     def jump(self, high):
#         return f"{self.name} прыгает на {high} см"
#
#     def run(self, long):
#         return f"{self.name} бегает по {long} км каждый день"
#
#     def bark(self, noise):
#         return f"{self.name} лает в {noise} db"
#
# puppy = Dog(30, 50, "Jakson", 6)
#
# print(puppy.__dict__)
# print(puppy.jump(30))
# print(puppy.run(10))
# print(puppy.bark(50))


# 14_2 Добавить в класс Dog метод change_name. Метод
# принимает на вход новое имя и меняет атрибут имени у
# объекта. Создать один объект класса. Вывести имя

class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

def change_name(self, name):
    name = input()
    puppy.name = name
    return puppy.name

def jump(self, high):
    return f"{self.name} прыгает на {high} см"


def run(self, long):
    return f"{self.name} бегает по {long} км каждый день"


def bark(self, noise):
    return f"{self.name} лает в {noise} db"

puppy = Dog (30, 50, "Jakson", 6)

print(puppy.name)
print(puppy.change_name())

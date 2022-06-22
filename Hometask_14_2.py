# 14_5 Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly, Cat - meow, Dog - bark.

# class Dog:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self, km):
#         return f"{self.name} can running {km}км"
#
#     def jump(self, m):
#         return f"{self.name} can jumping {m}м"
#
#     def birthday(self):
#         return f"Today {self.name}'s birthday and he is {self.age + 1}"
#
#     def sleep(self):
#         return f"{self.name} is sleeping"
#
#     def bark(self):
#         return f"{self.name} is barking"
#
#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self, km):
#         return f"{self.name} can running {km}км"
#
#     def jump(self, m):
#         return f"{self.name} can jumping {m}м"
#
#     def birthday(self):
#         return f"Today {self.name}'s birthday and he is {self.age + 1}"
#
#     def sleep(self):
#         return f"{self.name} is sleeping"
#
#     def meow(self):
#         return f"{self.name} is meowing"
#
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self, km):
#         return f"{self.name} can running {km}км"
#
#     def jump(self, m):
#         return f"{self.name} can jumping {m}м"
#
#     def birthday(self):
#         return f"Today {self.name}'s birthday and he is {self.age + 1}"
#
#     def sleep(self):
#         return f"{self.name} is sleeping"
#
#     def fly(self):
#         return f"{self.name} is flying"

# 14_6 Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet.
# Удалить в дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.

# class Pet:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self, km):
#         return f"{self.name} can running {km}км"
#
#     def jump(self, m):
#         return f"{self.name} can jumping {m}м"
#
#     def birthday(self):
#         return f"Today {self.name}'s birthday and he is {self.age + 1}"
#
#     def sleep(self):
#         return f"{self.name} is sleeping"
#
# Teddy = Pet('Teddy', 2, 'running')
# print(Teddy.run(4))
# print(Teddy.jump(1))
# print(Teddy.birthday())
# print(Teddy.sleep())
#
# class Dog(Pet):
#     def __init__(self, name, age, master):
#         super().__init__ (name, age, master)
#
#     def bark(self):
#         return f"{self.name} is barking"
#
# druzhok = Dog('Druzhok', 4, 'barking')
# print(druzhok.run(4))
# print(druzhok.jump(1))
# print(druzhok.birthday())
# print(druzhok.sleep())
# print(druzhok.bark())
#
# class Cat(Pet):
#     def __init__(self, name, age, master):
#         super().__init__ (name, age, master)
#
#     def meow(self):
#         return f"{self.name} is meowing"
#
# Bonia = Cat('Bonia', 3, 'meowing')
# print(Bonia.run(4))
# print(Bonia.jump(1))
# print(Bonia.birthday())
# print(Bonia.sleep())
# print(Bonia.meow())
#
# class Parrot(Pet):
#     def __init__(self, name, age, master):
#         super().__init__ (name, age, master)
#
#     def fly(self):
#         return f"{self.name} is flying"
#
# Kesha = Parrot('Kesha', 2, 'speaking')
# print(Kesha.run(4))
# print(Kesha.jump(1))
# print(Kesha.birthday())
# print(Kesha.sleep())
# print(Kesha.fly())
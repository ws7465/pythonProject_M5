#
# Домашняя работа по уроку "Атрибуты и методы объекта."
# #
# #
#   Задача "Developer - не только разработчик":
#   Реализуйте класс House, объекты которого будут создаваться
#   следующим образом:
#   House('ЖК Эльбрус', 30)
#   Объект этого класса должен обладать следующими атрибутами:
#   self.name - имя, self.number_of_floors - кол-во этажей
#   Также должен обладать методом go_to(new_floor),
#   где new_floor - номер этажа(int), на который нужно приехать.
#   Метод go_to выводит на экран(в консоль) значения
#   от 1 до new_floor(включительно).
#   Если же new_floor больше чем self.number_of_floors или меньше 1,
#   то вывести строку "Такого этажа не существует".
#
#   Пункты задачи:
#   1.	Создайте класс House.
#   2.	Вунтри класса House определите метод __init__,
#       в который передадите название и кол-во этажей.
#   3.	Внутри метода __init__ создайте атрибуты объекта self.name
#       и self.number_of_floors, присвойте им переданные значения.
#   4.	Создайте метод go_to с параметром new_floor и напишите
#       логику внутри него на основе описания задачи.
#   5.	Создайте объект класса House с произвольным названием
#       и количеством этажей.
#   6.	Вызовите метод go_to у этого объекта с произвольным числом.
# #
#
print(777)
# class House :
#     def __init__(self, name):
#         self.name = name
#         print(333)
#     # def __init__(self, name, number_of_floors):
#     #     self.name = name
#     #     self.number_of_floors = int(number_of_floors)
#     #     #self.new_floor = 0
#     #     #self.go_to(self.new_floor)
#         print(name)
#
#     def go_to(self, new_floor) :
#         self.new_floor = new_floor
#         if 1 <= self.new_floor <= self.number_of_floors :
#             for i in range(1, self.new_floor+1) :
#                 print(i)
#         # if 1 <= new_floor <= self.number_of_floors :
#         #     for i in range(1, new_floor+1) :
#         #         print(i)
#         else :
#             print("Такого этажа не существует")
# # #
# h1 = House('ЖК Горский')
print(444)
#h1.go_to(5)
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
##
##
#
# Пример результата выполнения программы:
# Исходные данные:
# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
#
# Вывод на консоль:
# 1
# 2
# 3
# 4
# 5
# "Такого этажа не существует"
#
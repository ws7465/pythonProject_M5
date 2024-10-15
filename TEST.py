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
#print(777)
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
#print(444)
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
#
# #
# # Задача "Магические здания":
# #
# # Для решения этой задачи будем пользоваться решением к предыдущей
# # задаче "Атрибуты и методы объекта".
# #
# # Необходимо дополнить класс House следующими специальными методами:
# #
# #     __len__(self) - должен возвращать кол-во этажей здания
# #                       self.number_of_floors.
# #     __str__(self) - должен возвращать строку:
# #                     "Название: <название>, кол-во этажей: <этажи>".
# #
# # # #
# #
# class House :
#       def __init__(self, name, number_of_floors) :
#          self.name = name
#          self.number_of_floors = int(number_of_floors)
# #
#       def go_to(self, new_floor) :
#          new_floor = int(new_floor)
#          if 1 <= new_floor <= self.number_of_floors :
#               for i in range(1, new_floor+1) :
#                   print(i)
#          else :
#               print("Такого этажа не существует")
# #
#       def __len__(self) :
#           return self.number_of_floors
# #
#       def __str__(self) :
#           return 'Название: '+self.name+', кол-во этажей: '+str(self.number_of_floors) #
#           #return f"Название: {self.name}, кол-во этажей: {self.number_of_floors} " #
# # # #
# #
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# print(str(h1))
# print(str(h2))
# print(len(h1))
# print(len(h2))
# #
# # Пример результата выполнения программы:
# # Пример выполняемого кода:
# # h1 = House('ЖК Эльбрус', 10)
# # h2 = House('ЖК Акация', 20)
# #
# # # __str__
# # print(h1)
# # print(h2)
# #
# # # __len__
# # print(len(h1))
# # print(len(h2))
# #
# # Вывод на консоль:
# # Название: ЖК Эльбрус, кол-во этажей: 10
# # Название: ЖК Акация, кол-во этажей: 20
# # 10
# # 20



#
class House :
      def __init__(self, name, number_of_floors) :
         self.name = name # наименование строения
         #self.number_of_floors = number_of_floors # кол-во его этажей
         self.number_of_floors = int(number_of_floors) # кол-во его этажей
#
      def go_to(self, new_floor) :
         new_floor = int(new_floor) # подъём на этаж строения
         if 1 <= new_floor <= self.number_of_floors :
              for i in range(1, new_floor+1) : # пройденные этажи
                  print(i)
         else :
              print("Такого этажа не существует")
#
      def __len__(self) :
         return self.number_of_floors # высота здания в этажах
#
      def __str__(self) : # характеристика строения
         return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'  #
#
###
      def __eq__(self, other):
          if isinstance(other, House):
              print('===========================')
              print(isinstance(other, House))
              print('===========================')
              h1 = int(self.number_of_floors)
              h2 = int(other.number_of_floors)
              print(self.number_of_floors)
              print(other.number_of_floors)
              return h1 == h2
          # elif not isinstance(other, House):
          #     print('+++++++++++++++++++++++++++++++++++')
          #     print(isinstance(other, House))
          #     print('+++++++++++++++++++++++++++++++++++')
          #     h1 = int(self.number_of_floors)
          #     h2 = int(other.number_of_floors)
          #     print(self.number_of_floors)
          #     #print(other.number_of_floors)
          #     return h1 == h2
      # def __eq__(self, other):
      #     if isinstance(other, House):
      #         print('===========================')
      #         print(isinstance(other, House))
      #         print('===========================')
      #         print(self.number_of_floors)
      #         print(other.number_of_floors)
      #         return self.number_of_floors == other.number_of_floors
      #     elif not isinstance(other, House):
      #         print('+++++++++++++++++++++++++++++++++++')
      #         print(isinstance(other, House))
      #         print('+++++++++++++++++++++++++++++++++++')
      #         print(self.number_of_floors)
      #         #print(other.number_of_floors)
      #         #return self.number_of_floors == other.number_of_floors
      #         return True
          #return self.number_of_floors == other.number_of_floors
          # print('+++++++++++++++++++++++++++++++++++')
          # print(isinstance(other, House))
          # print('+++++++++++++++++++++++++++++++++++')
          # print('self  ')
          # print(self.number_of_floors)
          # print(f'other ')
          # print(other.number_of_floors)
          # return False

      # class Shape:
      #     def __init__(self, area):
      #         self.area = area
      #
      #     def __eq__(self, other):
      #         if isinstance(other, Shape):
      #             return self.area == other.area
      #         return False
      #
      #     def __lt__(self, other):
      #         if isinstance(other, Shape):
      #             return self.area < other.area
      #         return False

      #def __eq__(self, other) : # True, если кол-во этажей одинаково у self и у other.
          #if (isinstance(self.number_of_floors, int) and isinstance(self, House)) and (isinstance(other.number_of_floors, int) and isinstance(other, House)) :  #
          #print(self.number_of_floors)
          #print(isinstance(self, House))
          #if 1 : #not isinstance(other, self.__class__) :
          #print('--------------------------------------------')
          #print(self.number_of_floors)
          #print(getattr(other, number_of_floors))
          #return self.number_of_floors == other
          #if isinstance(self, House) :  #
              #return self.number_of_floors == other.number_of_floors
          #else : #
          #    return 'ошибка в исходных данных'
          #return number_of_floors
          #return self.number_of_floors
####
      #
      # Шаг   # 1: определение    # класса
      #
      # class CustomNumber:
      #     def __init__(self, value):
      #
      #         self.value = value
      #
      # def __add__(self, other):
      #     if isinstance(other, CustomNumber):
      #         return CustomNumber(self.value + other.value)
      #
      # else:
      # return CustomNumber(self.value + other)
      #
      # def __radd__(self, other):
      #     return self.__add__(other)
      #
      # Шаг    # 2: демонстрация   # использования
      # a = CustomNumber(5)
      # b = CustomNumber(10)
      # print((a + b).value)  # Вывод: 15
      # print((a + 2).value)  # Вывод: 7
      # print((3 + a).value)  # Вывод: 8
      #
      def __add__(self, value):
          if isinstance(value, House):
              self.number_of_floors += value  #
              print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')  #
              return self.number_of_floors #
          else:
              return House(self.number_of_floors + value) #

      def __radd__(self, other):
          return self.__add__(other)
      #
      # Шаг
      # 2: демонстрация
      # использования
      # a = CustomNumber(5)
      # b = CustomNumber(10)
      # print((a + b).value)  # Вывод: 15
      # print((a + 2).value)  # Вывод: 7
      # print((3 + a).value)  # Вывод: 8
###
      # def __add__(self, value) : # добавить этажи
      #     self.number_of_floors += int(value) #
      #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'  #
#
# # #
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#
print(h1)
print(h2)
#
print(h1 == h2) # __eq__
#
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2) # __eq__
#
#h1 += 10 # __iadd__
#print(h1)
#
#h2 = 10 + h2 # __radd__
#print(h2)
#
#print(h1 > h2) # __gt__
#print(h1 >= h2) # __ge__
#print(h1 < h2) # __lt__
#print(h1 <= h2) # __le__
#print(h1 != h2) # __ne__
#
# # #
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# False
# Название: ЖК Эльбрус, кол-во этажей: 20
# True
# Название: ЖК Эльбрус, кол-во этажей: 30
# Название: ЖК Акация, кол-во этажей: 30
# False
# True
# False
# True
# False
#
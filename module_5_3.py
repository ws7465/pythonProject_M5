# #
#   Задача "Нужно больше этажей":
#
#   Для решения этой задачи будем пользоваться решением к предыдущей задаче
#   "Специальные методы класса".
#
#   Необходимо дополнить класс House следующими специальными методами:
#
#     __eq__(self, other) - должен возвращать True, если количество этажей одинаковое
#       у self и у other.
#     Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны
#       присутствовать в классе и возвращать результаты сравнения по
#       соответствующим операторам.
#       Как и в методе __eq__ в сравнении участвует кол-во этажей.
#     __add__(self, value) - увеличивает кол-во этажей на переданное
#       значение value, возвращает сам объект self.
#     __radd__(self, value), __iadd__(self, value) - работают так же как
#       и __add__ (возвращают результат его вызова).
#
#   Остальные методы арифметических операторов, где self - x, other - y:
#
#       Следует заметить, что other может быть не только числом,
#       но и вообще любым объектом другого класса.
#       Для более точной логики работы методов __eq__, __add__
#       и других методов сравнения и арифметики перед выполняемыми действиями
#       лучше убедиться в принадлежности к типу при помощи функции isinstance:
#       isinstance(other, int) - other указывает на объект типа int.
#       isinstance(other, House) - other указывает на объект типа House.
#
###
#
class House :
      def __init__(self, name, number_of_floors) :
         self.name = name # наименование строения
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
      def __eq__(self, other):
          if isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              return akh1 == akh2
          elif not isinstance(other, House):
              #print('+++++++++++++++++++++++++++++++++++')
              #print(isinstance(other, House))
              #print('+++++++++++++++++++++++++++++++++++')
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              #print(self.number_of_floors)
              #print(other)
              return akh1 == akh2
#
      def __add__(self, other):
          #self.number_of_floors += value  #
          if isinstance(other, House):
              #print('ak_add_if')
              akh = self.number_of_floors + other.number_of_floors
              print(f'Название: {self.name}, кол-во этажей: {akh}')  #
              return akh
          else :
              #print('ak_add_else')
              akh = self.number_of_floors + other
              print(f'Название: {self.name}, кол-во этажей: {akh}')  #
              return akh
#
#
      def __radd__(self, other):
          return self.__add__(other)
      ##
##########
#       def __add__(self, other):
#           if isinstance(other, CustomNumber):
#               return CustomNumber(self.value + other.value)
#
#       else:
#       return CustomNumber(self.value + other)
#
#       def __radd__(self, other):
#           return self.__add__(other)
# ##########
#
      def __lt__(self, other) : # True, если кол-во этажей одинаково у self и у other.
          if (isinstance(self.number_of_floors, int) and isinstance(self, House)) and (isinstance(other.number_of_floors, int) and isinstance(other, House)) :  #
              return self.number_of_floors < other.number_of_floors #
          else : #
              return 'ошибка в исходных данных'
#
      def __le__(self, other) : # True, если кол-во этажей одинаково у self и у other.
          if (isinstance(self.number_of_floors, int) and isinstance(self, House)) and (isinstance(other.number_of_floors, int) and isinstance(other, House)) :  #
              return self.number_of_floors <= other.number_of_floors #
          else : #
              return 'ошибка в исходных данных'
#
      def __gt__(self, other) : # True, если кол-во этажей одинаково у self и у other.
          if (isinstance(self.number_of_floors, int) and isinstance(self, House)) and (isinstance(other.number_of_floors, int) and isinstance(other, House)) :  #
              return self.number_of_floors > other.number_of_floors #
          else : #
              return 'ошибка в исходных данных'
#
      def __ge__(self, other) : # True, если кол-во этажей одинаково у self и у other.
          if (isinstance(self.number_of_floors, int) and isinstance(self, House)) and (isinstance(other.number_of_floors, int) and isinstance(other, House)) :  #
              return self.number_of_floors >= other.number_of_floors #
          else : #
              return 'ошибка в исходных данных'
#
      def __ne__(self, other) : # True, если кол-во этажей одинаково у self и у other.
          if (isinstance(self.number_of_floors, int) and isinstance(self, House)) and (isinstance(other.number_of_floors, int) and isinstance(other, House)) :  #
              return self.number_of_floors != other.number_of_floors #
          else : #
              return 'ошибка в исходных данных'
#
      # def __add__(self, value) : # добавить этажи
      #     self.number_of_floors += int(value) #
      #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'  #
# #
#       def __radd__(self, value) : # добавить этажи
#           #self.number_of_floors += int(value) #
#           #return self
#           return self + value
# #
#       def __iadd__(self, value) : # добавить этажи
#           #self.number_of_floors += int(value) #
#           #return self
#           return self + value
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
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# print(str(h1))
# print(str(h2))
# print(len(h1))
# print(len(h2))
###
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__
#
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
# Примечания:
#
#     Методы __iadd__ и __radd__ не обязательно описывать заново,
#     достаточно вернуть значение вызова __add__.
#
# Конец задания

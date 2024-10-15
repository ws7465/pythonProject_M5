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
      def __eq__(self, other) : #  True,если __eq__(==).
          if isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              return akh1 == akh2
          elif not isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              return akh1 == akh2
#
      def __add__(self, other) : # добавить (x + y)
           if isinstance(other, House):
              self.number_of_floors += other.number_of_floors
              return House(self.name, self.number_of_floors)
           else :
              self.number_of_floors += other
              return House(self.name, self.number_of_floors)
#
      def __radd__(self, other) : # отражённое сложение x + y
          return self.__add__(other)

      def __iadd__(self, other):  # сложение с присваиванием x += y
          self.number_of_floors = self.__add__(other)
          return self.number_of_floors
#
      def __lt__(self, other) : # True,если __lt__(<).
          if isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              return akh1 < akh2
          elif not isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              return akh1 < akh2
#
      def __le__(self, other) : # True, если , __le__(<=)
          if isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              return akh1 <= akh2
          elif not isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              return akh1 <= akh2
#
      def __gt__(self, other) : # True, если , __gt__(>)
          if isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              return akh1 > akh2
          elif not isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              return akh1 > akh2

#
      def __ge__(self, other) : # True, если , __ge__(>=)
          if isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              return akh1 >= akh2
          elif not isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              return akh1 >= akh2
#
      def __ne__(self, other) : # True, если , __ne__(!=)
          if isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              return akh1 != akh2
          elif not isinstance(other, House):
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              return akh1 != akh2
#
# # #
# Пример результата выполнения программы:
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
h1 += 10 # __iadd__
print(h1)
#
h2 = 10 + h2 # __radd__
print(h2)
#
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
#
# # #
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
#
#
# Конец задания
#

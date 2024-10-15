#
class House :
      def __init__(self, name, number_of_floors) :
         self.name = name # наименование строения
         #self.number_of_floors = number_of_floors # кол-во его этажей
         self.number_of_floors = int(number_of_floors) # кол-во его этажей
#
###
      def __eq__(self, other):
          if isinstance(other, House):
              print('===========================')
              print(isinstance(other, House))
              print('===========================')
              akh1 = int(self.number_of_floors)
              akh2 = int(other.number_of_floors)
              print(self.number_of_floors)
              print(other.number_of_floors)
              return akh1 == akh2
          elif not isinstance(other, House):
              print('+++++++++++++++++++++++++++++++++++')
              print(isinstance(other, House))
              print('+++++++++++++++++++++++++++++++++++')
              akh1 = int(self.number_of_floors)
              akh2 = int(other)
              print(self.number_of_floors)
              print(other)
              return akh1 == akh2
##
      def __add__(self, value):
          self.number_of_floors += value  #
          print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')  #
          return self.number_of_floors  #
          # if isinstance(value, House):
          #     self.number_of_floors += value  #
          #     print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')  #
          #     return self.number_of_floors #
          # else:
          #     return self.number_of_floors #

      def __radd__(self, other):
          return self.__add__(other)
      #
##
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

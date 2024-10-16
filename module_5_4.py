#
# # # # Задача "История строительства":
#
# Для решения этой задачи будем пользоваться решением к предыдущей задаче
# "Перегрузка операторов".
#
# В классе House создайте атрибут houses_history = [],
# который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта,
# тем более можно удобно обращаться к атрибутам класса используя ссылку
# на сам класс - cls.
#
# Дополните метод __new__ так, чтобы:
#
#     Название объекта добавлялось в список cls.houses_history.
#     Название строения можно взять из args по индексу.
#
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
#       "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.
#
# # # #
#
class House : #
    houses_history = [] # add 5_4
#


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
#
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
# # # #
#
# Пример результата выполнения программы:
#
# Пример выполнения программы:
# h1 = House('ЖК Эльбрус', 10)
# print(House.houses_history)
# h2 = House('ЖК Акация', 20)
# print(House.houses_history)
# h3 = House('ЖК Матрёшки', 20)
# print(House.houses_history)
#
# # Удаление объектов
# del h2
# del h3
#
# print(House.houses_history)
#
# Вывод на консоль:
# ['ЖК Эльбрус']
# ['ЖК Эльбрус', 'ЖК Акация']
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Акация снесён, но он останется в истории
# ЖК Матрёшки снесён, но он останется в истории
# ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# ЖК Эльбрус снесён, но он останется в истории
#
#
# # # #   конец задания
#


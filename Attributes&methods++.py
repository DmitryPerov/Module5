class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def __lt__(self, other):
        if isinstance (other , int):
            return self.number_of_floors < other
        elif isinstance (other, House):
            return  self.number_of_floors < other.number_of_floors
        else:
            raise TypeError("Не поддерживаемый тип для сравнения")

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > ether
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            raise TypeError ("Неподдерживаемый тип для сравнения")

    def __le__(self, other):
        if isinstance (other, int):
            return self.number_of_floors <= other
        elif isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise TypeError ("Неподдерживаемый тип для сравнения")

    def __ge__(self, other):
        if isinstance (other, int):
            return other.number_of_floors >= other
        elif isinstance (other, House):
            return other.number_of_floors >= other.number_of_floors
        else:
            raise TypeError("Неподдерживаемый тип для сравнения")

    def __add__(self, _value):
        if isinstance(_value, House):
            return (self.number_of_floors + _value.number_of_floors)
        elif isinstance(_value, int):
            self.number_of_floors += _value
            return self
        else:
            raise TypeError("Неподдерживаемый тип для данной операции")

    def __radd__(self, other):
        return self.__add__(other)

    def __ne__(self, other):
        if isinstance (other, int):
            return other.number_of_floors != other
        elif isinstance (other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            raise TypeError("Неподдерживаемый тип для сравнения")

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

# Пример
print("--------------------")
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1, type(h1))
print(h2, type(h2))

print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1, type(h1))

print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2, type(h2))

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__







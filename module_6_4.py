class Figure:
    sides_count = 0

    def __init__(self, rgb, *sides):
        self.__color = list(rgb)
        self.__sides = []

        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

        self.filled = True # фигура изначально закрашена

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in new_sides))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def get_square (self):
        __radius = self.get_sides()[0] / (2 * 3.14)
        return 3.14 * (__radius **2)

class Triangle(Figure):
    sides_count = 3

    def get_square (self):
        a, b, c = self.get_sides() #
        s = (a + b + c) / 2  # Полупериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Площадь по формуле Герона

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides_length):
        super().__init__(color, sides_length)
        self.__sides = [sides_length] * self.sides_count  # Создаем список из 12 одинаковых сторон

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())







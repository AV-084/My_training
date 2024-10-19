class Figure:
    sides_count = 0

    def __init__(self, rgb, *sides):
        self.__color = list(rgb)  # Инициализируем цвет фигуры
        if len(sides) == self.sides_count:  # Проверяем, совпадает ли количество сторон с sides_count
            self.__sides = list(sides)  # Сохраняем стороны
        else:
            self.__sides = [1] * self.sides_count  # Если нет, создаем список из единиц
        self.filled = True  # Фигура изначально закрашена

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):  # Проверяем корректность цвета
            self.__color = [r, g, b]  # Устанавливаем новый цвет

    def __is_valid_sides(self, *new_sides):
        return (len(new_sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in new_sides))

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):  # Проверяем, допустимы ли новые стороны
            self.__sides = list(new_sides)  # Устанавливаем новые стороны

class Circle(Figure):
    sides_count = 1

    def get_square(self):
        __radius = self.get_sides()[0] / (2 * 3.14159)
        return 3.14159 * (__radius ** 2)  # Площадь круга: π * r²

class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Площадь по формуле Герона

class Cube(Figure):
    sides_count = 12  # У куба 12 ребер

    def __init__(self, color, side_length):
        super().__init__(color, side_length)  # Вызываем конструктор родительского класса
        self.__sides = [side_length] * self.sides_count  # Создаем список из 12 одинаковых сторон

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3  # Объем куба: a³


circle1 = Circle((200, 200, 100), 10)  # Круг с цветом и длиной окружности
cube1 = Cube((222, 35, 130), 6)  # Куб с цветом и длиной ребра

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Устанавливаем новый цвет для круга (изменится)
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Некорректный цвет
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Некорректные стороны (не изменится)
print(cube1.get_sides())
circle1.set_sides(15)  # Устанавливаем новую длину окружности для круга (изменится)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объема (куба):
print(cube1.get_volume())










































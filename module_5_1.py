class House:
    def __init__(self, name, number_of_floors):
        # инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # проверка допустимости
        if 0 < new_floor <= self.number_of_floors:
            # вывод последовательности чисел от 1 до new_floor
            for floor in range (1, new_floor + 1):
                print(floor)
        else:
            # сообщение об ошибке
            print('Такого этажа не существует')

# пример использования класса
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# вызов метода go_to
h1.go_to(5)
h2.go_to(10)




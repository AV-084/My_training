class House: # Объявления класса
    def __init__(self, name, number_of_floors): # Метод инициализации
        self.name = name # Установка значений атрибутов
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Названиие: {self.name}, кол-во: {self.number_of_floors}'

# Пример использования класса
h1 = House('ЖК Эльбрус', 10) # Создание экземпляра
h2 = House('Акация', 20) # Создание экземпляра

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

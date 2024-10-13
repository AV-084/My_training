class Animal:
    alive = True # живой
    fed = False # не накормленный

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    edible = False # не съедобный

    def __init__(self, name):
        self.name = name

class Predator(Animal):
    pass # метод eat наследуется из базового (родительского) класса

class Mammal(Animal):
    pass # метод eat наследуется из базового (родительского) класса

class Flower(Plant):
    pass
    # не съедобное

class Fruit(Plant):
    edible = True # съедобное

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
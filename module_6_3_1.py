import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self):
        if self.sound:
            print(self.sound)

class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        'Ныряем, уменьшая координату Z и снижая скорость в два раза'
        self.speed /= 2
        dz = abs(dz)
        self._cords[2] -= int(dz * self.speed)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(6)
db.get_cords()

db.lay_eggs()  # случайное число от 1 до 4
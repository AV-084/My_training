import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)  # вместо метода super
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        enemies = 100
        while enemies:
            enemies -= self.power
            days +=1
            print(f'{self.name} сражался {days} дней (дня)..., осталось {enemies} воинов ')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
import threading
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            x = randint(50,500)
            with self.lock: # Блокировка для безопасного изменения баланса
                self.balance += x
                print(f'Пополнение:{x}. Баланс:{self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            y = randint(50, 500)
            with self.lock: # Блокировка для безопасного изменения баланса
                print(f'Запрос на {y}')
                if y <= self.balance:
                    self.balance -= y
                    print(f'Снятие:{y}. Баланс:{self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join() # Основной поток ждет, пока th1 (пополнение) завершится.
th2.join() # Основной поток ждет, пока th2 (снятие) завершится.

print(f'Итоговый баланс: {bk.balance}')

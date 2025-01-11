def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        if res <  2:
            print("Не является ни простым, ни составным")

        prime = True
        for i in range(2, int(res ** 0.5) + 1): # так как делители числа всегда находятся до его квадратного корня
            if res % i == 0:
                prime = False
                break

        if prime:
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
   if i == 1:
       continue
   # print(i)
   is_prime = True
   for j in range (2, i):
        # print(f'{i} {j} {i/j}')
        if i % j == 0:
            is_prime = False
            # print (is_prime)
            break
   if is_prime:
       # print (is_prime)
       primes.append(i)
   else:
       not_primes.append(i)

print(f'''{'Primes:'} {primes}
{'Not Primes:'} {not_primes}''')
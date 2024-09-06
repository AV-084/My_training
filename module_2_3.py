my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = -1
while n >= -1:
    n = n + 1
    if my_list[n] < 0 or n == len(my_list):
        break
    if my_list[n] == 0:
        continue
    print (my_list[n])

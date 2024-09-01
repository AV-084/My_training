# кортеж из чисел, списков, строк, других кортежей, логических значений

mixed_tuple = (1, 2.5, [1, 2, 3], 'String', (1, 2), True, False)
print(mixed_tuple)

immutable_var = (1, 2.5, [1, 2, 3], 'String', (1, 2), True, False)
immutable_var [0] = 10
# изменение элементов кортежа невозможно, т.к. кортеж - это неизменяемый тип данных

mutable_list = [1, 2.5, [1, 2, 3], 'String', (1, 2), True, False]
mutable_list [2] = 'Modified'
print(mutable_list)


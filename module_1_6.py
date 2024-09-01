my_dict = {'Max': 2000, 'David': 2005, 'Alex': 1999}
print('Dict:', my_dict)
print('Existing value:', my_dict ['Max'])
print ('Not existing value:', my_dict.get ('Irina'))
my_dict.update({'Vadim': 1976,
                'Sveta': 1980})
print ('Deleted value:', my_dict.pop ('Max'))
print('Modified dictionary:', my_dict)
print('')

my_set = {1, 2, 3, 3, 2, 'String', 4.25, 'String', 4.25,}
print('Set:', my_set)
my_set.add (10)
my_set.add ((2, 5, 6))
my_set.discard('String')
print('Modified set:', my_set)



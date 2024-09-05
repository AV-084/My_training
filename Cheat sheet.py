
int     # числа целые
float   # числа с плавающей запятой (десятичные)
complex # числа (x+yj)
a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))
#(1+2j) is complex number? True

list  # списки [ ] изменяемая упорядоченная последовательность элементов разных типов
      # возможен доcтуп по индексу и извлечение среза []
a = [1, 2.2, 'python']

tuple # кортежи ( ) неизменяемая упорядоченная последовательность элементов разных типов
      # возможен допуск по индексу и извлечение среза []
tuple_ = (1, 2.5, 1+3j, [1, 2, 3], 'String', (1, 2), True, False)

str # строки '' неизменяемая последовательность символов
    # возможен допуск по индексу и извлечение среза []
s = "Простая строка"
s = '''многострочная
строка'''

set # множества {} неупорядоченная последовательность с уникальными объектами
    # объединение и пересечение, дубликаты автоудаляются
    # т.к. неупорядочено - операторы извлечения/среза не работают
a = {5,2,3,1,4}

dict # словари {} неупорядоченные наборы пар ключ-значение
d = {1:'value', 'key':2}

# Преобразование типов данных с помощью таких функций, как int(), float(), str() и т.д.
int(-10.6)
-10
float('2.5')
2.5
str(25)
'25'
set([1, 2, 3, 4])
{1, 2, 3, 4}
tuple({5,6,7})
(5, 6, 7)

# из строки в список символов:
list('hello')
['h', 'e', 'l', 'l', 'o']

# Для преобразования списка из символов обратно в строку:
''.join(['h', 'e', 'l', 'l', 'o'])

# Для преобразования в словарь каждый элемент последовательности должен быть парой:
dict([[1,2],[3,4]])
{1: 2, 3: 4}

dict([(3,26),(4,44)])
{3: 26, 4: 44}



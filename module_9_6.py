def all_variants(text):
   for length in range(1, len(text) + 1): # Перебираем длины подпоследовательностей от 1 до длины строки
        for start in range(len(text) - length + 1): # Для каждой длины создаем подпоследовательности
            yield text[start:start + length]# Генерируем срез строки

a = all_variants("abc")
for i in a:
    print(i)
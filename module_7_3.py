class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower() # Читаем файл и приводим текст к нижнему регистру
                for char in ['.', ',', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(char, '') # Убираем пунктуацию
                words = text.split() # Разбиваем текст на слова
                all_words.update ({file_name: words})
                # all_words [file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        word = word.lower()  # Игнорируем регистр
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # Позиция с 1
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        word = word.lower()  # Игнорируем регистр
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)  # Количество вхождений
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
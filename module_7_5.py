import os
import time

directory = '.' # Указываем директорию, в которой будем искать файлы ('.' - текущая директория)

for root, dirs, files in os.walk(directory): # Проходим по всем поддиректориям и файлам в указанной директории
    for file in files: # Перебираем все файлы в текущей директории
        filepath = os.path.join(root, file) # Формируем полный путь к файлу, используя os.path.join
        filetime = os.path.getatime(filepath) # Получаем время последнего изменения файла в формате Unix (число секунд с 1 января 1970)
        # Форматируем время в удобочитаемый вид (дд.мм.гггг чч:мм)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath) # Получаем размер файла в байтах
        parent_dir = os.path.dirname(filepath) # Получаем родительскую директорию файла
        # parent_dir = root  # то же самое
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}'
        )
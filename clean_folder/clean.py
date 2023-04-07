from pathlib import Path
import re
import sys
import shutil



CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
            "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
CYRILLIC_SYMBOLS = tuple(CYRILLIC_SYMBOLS)
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


new_folder = Path('Garbage')
new_folder.mkdir(exist_ok=True)


EXTENSIONS_DICT = {
    'images': ('.jpeg', '.png', '.jpg', '.svg', '.dng'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xls', '.xlsx', '.pptx', '.djvu', '.rtf'),
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'archives': ('.zip', '.gz', '.tar'),
    'photoshop': ('.xmp', '.nef'),
    'books': ('.epub', '.fb2')
}


def main():
    if len(sys.argv) < 2:
        print ('no iterable folders in path')
        exit()
    folder_iterable = Path(sys.argv[1])
    sort (folder_iterable)


def normalize(name):
    name.translate(TRANS)
    new_name = re.sub(r'\W','_',name)
    return new_name


def sort(folder_name: Path):
    for item in folder_name.iterdir():
        if item.is_dir():
            sort(item)
        else:
            suffix = item.suffix
            file = item.stem
            file = (normalize(file))
            norm_item = file + suffix
            print(norm_item)
            for key, values in EXTENSIONS_DICT.items():
                if suffix in EXTENSIONS_DICT['archives']:
                    new_path = new_folder / key
                    new_path.mkdir(exist_ok=True, parents=True)
                    shutil.unpack_archive(item, new_path)
                    continue
                if suffix in values:
                    new_path = new_folder/key
                    new_path.mkdir(exist_ok=True, parents=True)
                    print(new_path.absolute())
                    shutil.copyfile(item, new_path/norm_item)

if __name__ == '__main__':
    main()

import os
import shutil
import threading


def sort_files_by_extension(folder_path):
    # Отримання списку файлів та папок у вказаній директорії
    files = os.listdir(folder_path)

    # Створення словника для зберігання файлів за розширеннями
    file_extensions = {}

    # Проходження по кожному файлу та його розширенню
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in file_extensions:
                file_extensions[file_extension].append(file_path)
            else:
                file_extensions[file_extension] = [file_path]

    # Перенесення файлів за розширеннями в окремі папки
    for extension, files in file_extensions.items():
        folder_name = extension.replace(".", "") + "_files"
        folder_path = os.path.join(os.getcwd(), folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Створення потоку для копіювання файлів у нову папку
        def copy_files(files, folder_path):
            for file in files:
                shutil.move(file, folder_path)

        # Запуск потоку копіювання файлів
        thread = threading.Thread(target=copy_files, args=(files, folder_path))
        thread.start()


def process_folder(folder_path):
    # Отримання списку файлів та папок у вказаній директорії
    files = os.listdir(folder_path)

    # Обробка кожного підкаталогу в окремому потоці
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            thread = threading.Thread(target=process_folder, args=(file_path,))
            thread.start()

    # Сортування файлів за розширеннями
    sort_files_by_extension(folder_path)


if __name__ == "__main__":
    folder_path = "Хлам"
    process_folder(folder_path)

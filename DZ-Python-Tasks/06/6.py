from pathlib import Path

path = Path(input("Введите путь к каталогу: "))

files_count = 0
dirs_count = 0
py_files = []
total_size = 0

for item in path.iterdir():
    if item.is_file():
        files_count += 1
        total_size += item.stat().st_size
        if item.suffix == ".py":
            py_files.append(item.name)
    elif item.is_dir():
        dirs_count += 1

print("Количество файлов:", files_count)
print("Количество подкаталогов:", dirs_count)
print("Список всех .py файлов:", py_files)
print("Суммарный размер всех файлов:", total_size)

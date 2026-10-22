def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Файл не найден")
    except PermissionError:
        print("Нет прав доступа к файлу")
    except IsADirectoryError:
        print("Указанный путь является каталогом, а не файлом")
    except OSError as e:
        print("Ошибка операционной системы:", e)
    return None


content = read_file("data.txt")
if content is not None:
    print(content)

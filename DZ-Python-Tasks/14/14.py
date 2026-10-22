from contextlib import contextmanager


@contextmanager
def log_operation(filename, operation_name):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"START: {operation_name}\n")
        try:
            yield
            f.write(f"END: {operation_name}\n")
        except Exception:
            f.write(f"ERROR: {operation_name}\n")
            raise


with log_operation("operation.log", "Data processing"):
    print("Обработка данных...")
    x = 1 + 1

try:
    with log_operation("operation.log", "Bad operation"):
        raise ValueError("ошибка")
except ValueError:
    print("Исключение поймано снаружи")

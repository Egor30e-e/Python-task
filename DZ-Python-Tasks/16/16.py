import re
from collections import Counter

levels = Counter()
error_users = set()

pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (INFO|WARNING|ERROR) User (\d+)")

with open("logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            level = match.group(1)
            user_id = match.group(2)
            levels[level] += 1
            if level == "ERROR":
                error_users.add(user_id)

for level in ("INFO", "WARNING", "ERROR"):
    print(f"{level}: {levels.get(level, 0)}")

print("Пользователи с ошибками:", ", ".join(sorted(error_users)))

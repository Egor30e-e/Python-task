import re
import json
import logging
from collections import Counter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("processing.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

pattern = re.compile(
    r"(?P<ip>\d+\.\d+\.\d+\.\d+)\s+"
    r"(?P<method>GET|POST|PUT|DELETE|PATCH)\s+"
    r"(?P<url>\S+)\s+"
    r"(?P<code>\d{3})"
)

methods = Counter()
urls = Counter()
errors_4xx = 0

try:
    logging.info("Начало обработки логов")
    with open("access.log", "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                data = match.groupdict()
                methods[data["method"]] += 1
                urls[data["url"]] += 1
                code = int(data["code"])
                if 400 <= code < 500:
                    errors_4xx += 1
                logging.info(f"Обработана строка: {data['ip']} {data['method']} {data['url']} {data['code']}")
            else:
                logging.warning(f"Не удалось разобрать строку: {line.strip()}")

    most_common_url = urls.most_common(1)[0][0] if urls else None

    stats = {
        "methods": dict(methods),
        "errors_4xx": errors_4xx,
        "most_common_url": most_common_url,
        "url_counts": dict(urls)
    }

    with open("stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    logging.info("Статистика сохранена в stats.json")
    print("Статистика:")
    print(json.dumps(stats, ensure_ascii=False, indent=2))

except FileNotFoundError:
    logging.error("Файл access.log не найден")
except OSError as e:
    logging.error(f"Ошибка чтения файла: {e}")

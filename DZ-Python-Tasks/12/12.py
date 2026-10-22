import re

text = """Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru
"""

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
unique_emails = list(dict.fromkeys(emails))

for email in unique_emails:
    print(email)

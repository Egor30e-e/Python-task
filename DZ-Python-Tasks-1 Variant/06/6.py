from faker import Faker
import random


def gen(filename, count=1000):
    fake = Faker("ru_RU")

    with open(filename, "w", encoding="utf-8") as file:
        for i in range(count):
            name = fake.name()
            score = random.randint(0, 100)
            file.write(f"{name};{score}\n")


def get_stats(filename):
    minimum = None
    maximum = None
    best_name = None
    total = 0
    count = 0
    passed = 0

    with open(filename, "r", encoding="utf-8") as file:
        for l in file:
            parts = l.strip().split(";")
            if len(parts) != 2:
                continue

            name = parts[0].strip()
            score_text = parts[1].strip()

            if not name or not score_text.isdecimal():
                continue

            score = int(score_text)

            if score > 100:
                continue

            total += score
            count += 1

            if score >= 60:
                passed += 1

            if minimum is None or score < minimum:
                minimum = score

            if maximum is None or score > maximum:
                maximum = score
                best_name = name

    if count == 0:
        return None

    return total / count, maximum, minimum, passed, best_name


gen("students.txt", 1000)
result = get_stats("students.txt")

average, maximum, minimum, passed, best_name = result
print("AVG:", average)
print("MAX:", maximum)
print("MIN:", minimum)
print(">60:", passed)
print("BEST:", best_name)

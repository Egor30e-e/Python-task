def avg(numbers, k):
    if k < 0 or k > len(numbers):
        print("Ошибка, k должно быть от 1 до длины списка")
        return 0
    if isinstance(k, bool) or not isinstance(k, int):
        print("k должно быть целым числом")
        return 0
    result = []
    for i in range(len(numbers) - k + 1):
        window = numbers[i:i + k]
        avg = sum(window) / k
        result.append(avg)
    return result


print(avg([2, 4, 6, 8, 10], 3))

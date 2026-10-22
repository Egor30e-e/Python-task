

def compression(numbers):
    if len(numbers) == 0:
        return []

    result = []

    curr = numbers[0]  # 1
    cnt = 1

    for i in numbers[1:]:
        if i == curr:
            cnt += 1
        else:
            result.append((curr, cnt))
            curr = i
            cnt = 1
    result.append((curr, cnt))

    return result


print(compression([1, 1, 1, 2, 2, 5, 5, 5, 5, 3]))



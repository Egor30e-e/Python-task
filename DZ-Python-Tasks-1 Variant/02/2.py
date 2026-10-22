def very_unusual_string():  
    best = ""
    len_best = 0

    while True:
        text = input()

        if text == "STOP":
            break

        lenn = len(set(text.lower()))
        if lenn > len_best:
            len_best = lenn
            best = text

    print(best, len_best)


very_unusual_string()

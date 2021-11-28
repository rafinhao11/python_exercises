for i in range(1, 11):
    r = i - 2 * int(i / 2)
    if r != 0:
        fat = 1
        for j in range(1, i + 1):
            fat = fat * j
        print(fat)  
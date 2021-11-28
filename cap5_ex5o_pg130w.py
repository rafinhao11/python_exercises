i = 1
fat = 1
while i <= 10:
    r = i - 2 * int(i / 2)
    if r != 0:
        fat = fat * i
        print(fat)   
    i = i + 1
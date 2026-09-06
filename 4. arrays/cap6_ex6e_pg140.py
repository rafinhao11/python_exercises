a = []
b = []

for i in range(15):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for i in a:
    fat = 1
    j = 1
    for j in range(1, i + 1):
        fat = fat * j
    b.append(fat)

for i, j in zip(a, b):
    print(i, j)

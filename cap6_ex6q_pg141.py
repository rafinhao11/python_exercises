a = []
b = []

for i in range(15):
    n = float(input('Digite um valor numérico: '))
    a.append(n)

for i in range(15):
    if i % 2 == 0:
        b.append(a[i] / 2)
    else:
        b.append(a[i] * 1.5)

print(b)
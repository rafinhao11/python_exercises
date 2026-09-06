a = []
b = []

for i in range(10):
    n = int(input('Digite um valor numérico: '))
    if n >= 0:
        a.append(n)
    else:
        n = int(input('Digite um valor numérico positivo: '))
        a.append(n)

for i in a:
    i = i * (-1)
    b.append(i)

print(b)
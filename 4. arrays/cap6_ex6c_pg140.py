a = []
b = []
c = []

for i in range(20):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for i in range(20):
    n = int(input('Digite um valor numérico: '))
    b.append(n)

for i, j in zip(a, b):
    c.append(i - j)

for i in c:
    print(i)
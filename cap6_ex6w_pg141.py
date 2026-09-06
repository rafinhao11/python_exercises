a = []
b = []
c = []

for i in range(10):
    a.append(int(input('Digite um valor numérico: ')))
    b.append(int(input('Digite um valor numérico: ')))

for i in range(10):
    c.append((a[i] + b[i]) ** 2)

print(c)
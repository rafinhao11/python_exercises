a = []
b = []

for i in range(20):
    n = float(input('Digite um valor numérico: '))
    a.append(n)

for i in range(1, len(a) + 1):
    b.append(a[-i])

print(b)
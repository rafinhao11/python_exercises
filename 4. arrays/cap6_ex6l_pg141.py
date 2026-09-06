a = []
b = []

for i in range(10):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for i in a:
    i = i // 2
    b.append(i)

print(b)
a = []
b = []

for i in range(6):
    n = int(input('Digite um valor numérico: '))

    if n % 2 == 0:
        a.append(n)
    else:
        b.append(n)


c = []
c = a + b

print(c)
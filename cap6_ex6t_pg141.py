a = []
b = []

for i in range(10):
    n = int(input('Digite um valor numérico: '))

    if n % 2 == 0 and n % 3 == 0:
        a.append(n)
    else:
        if n % 5 == 0:
            b.append(n)

c = []

c = a + b

print(c)

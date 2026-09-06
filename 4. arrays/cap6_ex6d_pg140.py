a = []
b = []

for i in range(15):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for i in a:
    valor = i ** 2
    b.append(valor)

for i in b:
    print(i)
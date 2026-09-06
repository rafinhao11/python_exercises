a = []
b = []

for i in range(8):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for i in a:
    valor = i * 3
    b.append(valor)

for i in b:
    print(i)
a = []
b = []
c = []

for i in range(15):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for i in range(15):
    n = int(input('Digite um valor numérico: '))
    b.append(n)

c = a + b

for i in c:
    print(i)
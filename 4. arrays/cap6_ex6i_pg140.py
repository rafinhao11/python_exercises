a = []
b = []
c = []
d = []

for i in range(5):
    n = float(input('Digite um número: '))
    a.append(n)

for i in range(5):
    n = float(input('Digite um número: '))
    b.append(n)

for i in range(5):
    n = float(input('Digite um número: '))
    c.append(n)

d = a + b + c

print(d)
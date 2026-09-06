a = []
b = []

for i in range(12):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for i in a:
    if i % 2 == 1:
        impar = i * 2 
        b.append(impar)
    else:
        b.append(i)

print(b)
a = []
b = []
c = []
d = []

for i in range(6):
    a.append(int(input('Digite um valor numérico: ')))
    b.append(int(input('Digite um valor numérico: ')))

for i in range(6):
    if i % 2 == 0:
        d.append(a[i])
        d.append(b[i])
    else:
        c.append(a[i])
        c.append(b[i])

print(c)
print(d)

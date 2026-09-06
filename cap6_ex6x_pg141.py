a = []
b = []

for i in range(6):
    a.append(int(input('Digite um valor numérico: ')))

b = [0.0] * 6

for i in range(6):
    if i % 2 == 0:
        b[i] = a[i + 1]
    else:
        b[i] = a[i - 1]

print(a)
print(b)
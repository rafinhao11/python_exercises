a = []
b = []

for i in range(25):
    n = float(input('Digite o valor da temperatura em Celsius: '))
    a.append(n)

for c in a:
    f = (9 * c + 160) / 5
    b.append(f)

print(b)
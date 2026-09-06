a = []
par = 0

for i in range(15):
    n = int(input('Digite um valor numérico: '))
    a.append(n)
    if n % 2 == 0:
        par += 1

print(par)
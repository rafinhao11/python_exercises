a = []
par = 0
impar = 0

for i in range(30):
    n = int(input('Digite um valor numérico: '))
    if n % 2 == 0:
        a.append(n)
        par += 1
    else:
        a.append(n)
        impar += 1

print(par, impar)
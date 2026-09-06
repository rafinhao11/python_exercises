a = []
impar = 0

for i in range(10):
    n = int(input('Digite um valor numérico: '))
    a.append(n)
    if n % 2 != 0:
        impar += 1

print(impar)
a = []
b = []

for i in range(20):
    n = int(input('Digite um valor numérico: '))
    a.append(n)

for n in a:
    soma = 0
    soma = n * (n + 1) // 2
    b.append(soma)
    
print(b)
soma = 0
i = 1
while i <= 3:
    n = int(input("Digite um valor: "))
    fat = 1
    j = 1
    while j <= n:
        fat = fat * j
        j = j + 1
    soma = soma + fat
    i = i + 1
print(soma)
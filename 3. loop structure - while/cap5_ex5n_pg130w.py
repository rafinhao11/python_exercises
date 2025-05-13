soma = 0
n = 0
total = 0
while n >= 0:
    n = int(input("Digite o valor: "))
    if n >= 0:
        soma = soma + n
    total = total + 1
media = soma / total
print(soma, media)
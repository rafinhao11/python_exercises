n = int(input("Digite o valor: "))
valor_menor = n
valor_maior = n
while n >= 0:
    if valor_maior < n:
        valor_maior = n
    if valor_menor > n:
        valor_menor = n
    n = int(input("Digite um valor: "))
print(valor_menor, valor_maior)
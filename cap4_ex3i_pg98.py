a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
d = int(input("D: "))
e = int(input("E: "))

valor_maior = a
if valor_maior < b:
    valor_maior = b
if valor_maior < c:
    valor_maior = c
if valor_maior < d:
    valor_maior = d
if valor_maior < e:
    valor_maior = e

valor_menor = a
if valor_menor > b:
    valor_menor = b
if valor_menor > c:
    valor_menor = c
if valor_menor > d:
    valor_menor = d
if valor_menor > e:
    valor_menor = e

print(valor_menor, valor_maior)
soma = 0
cont = 0
for i in range(50, 71):
    r = i - 2 * int(i / 2)
    if r == 0:
        soma = soma + i
        cont = cont + 1
media = soma / cont
print(soma, media)
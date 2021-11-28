soma = 0
i = 50
while i <= 70:
    r = i - 2 * int(i / 2)
    if r == 0:
        soma = soma + i
    i = i + 1
media = soma / i
print(soma, media)
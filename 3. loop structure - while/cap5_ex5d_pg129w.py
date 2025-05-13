soma = 0
i = 1
while i <= 500:
    r = i - 2 * int(i / 2)
    if (r == 0):
        soma = soma + i
    i = i + 1
print(soma)
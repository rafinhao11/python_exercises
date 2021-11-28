soma = 0
for i in range(1, 500):
    r = i - 2 * int(i / 2)
    if r == 0:
        soma = soma + i
print(soma)
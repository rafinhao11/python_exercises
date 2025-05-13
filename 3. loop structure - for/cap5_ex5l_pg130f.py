soma = 0
for i in range (1, 16):
    fat = 1
    j = 1
    for j in range(1, i):
        fat = fat * j
        j = j + 1
    soma = soma + fat
print(soma)
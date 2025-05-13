base = int(input("Digite o valor base: "))
expoente = int(input("Digite o valor expoente: "))
i = 1
p = 1
while i <= expoente:
    p = p * base
    i = i + 1
print(p)
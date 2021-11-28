base = int(input("Digite a valor da base: "))
expoente = int(input("Digite o valor do expoente: "))
p = 1
for i in range(expoente):
    p = p * base
print(p)
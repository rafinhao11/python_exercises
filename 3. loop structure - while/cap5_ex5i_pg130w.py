i = 1
anterior = 0
atual = 1
print(anterior)
print(atual)
while i <= 15:
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    print(atual)
    i = i + 1
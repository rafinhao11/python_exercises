anterior = 0
atual = 1
for i in range(1, 15):
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    print(atual)
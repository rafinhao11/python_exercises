a = []
b = []
c = []

for i in range(20):
    nome = input('Digite um nome: ')
    a.append(nome)

for i in range(30):
    nome = input('Digite um nome: ')
    b.append(nome)

c = a + b

for i in c:
    print(i)
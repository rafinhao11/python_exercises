n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))


md1 = (n1 + n2 + n3 + n4) / 4
if (md1 >= 7):
    print("Aprovado", md1)
else:
    ne = float(input("Nota de Exame: "))
    md2 = (md1 + ne) / 2

    if (md2 >= 5 ):
        print("Aprovado por exame", md2)
    else:
        print("Reprovado por exame")
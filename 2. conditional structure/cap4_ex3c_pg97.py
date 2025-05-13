n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

md = (n1 + n2 + n3 + n4) / 4
if (md >= 5):
    print("Aprovado", md)
else:
    print("Reprovado", md)

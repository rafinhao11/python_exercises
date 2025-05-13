a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

#delta < 0 (não há resultados reais)
#delta = 0 (a equação possui um resultado real ou dois resultados iguais)
#delta > 0 (a equação possui dois resultados distintos)

#fórmula delta
#delta = b^2 - 4.a.c
delta = (b ** 2) - 4 * a * c

#fórmula de Bhaskara
#x = -b / 2.a
#x1 = (-b + RaizQ(delta)) / 2.a
#x2 = (-b - RaiQ(delta)) / 2.a
if (delta < 0):
    print("Não há resultados reais")
else:
    if (delta == 0):
        x = -b / 2 * a
        print(x)
    else:
        x1 = (-b + d ** (1/2)) / 2 * a
        x2 = (-b - d ** (1/2)) / 2 * a
        print(x1, x2)

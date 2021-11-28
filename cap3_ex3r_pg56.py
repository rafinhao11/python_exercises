a = int(input("Candidato A: "))
b = int(input("Candidato B: "))
c = int(input("Candidato C: "))
vn = int(input("Votos Nulos: "))
vb = int(input("Votos Brancos: "))

total_eleitores = a + b + c + vn + vb
perc_a = int(a * 100 / total_eleitores)
perc_b = int(b * 100 / total_eleitores)
perc_c = int(c * 100 / total_eleitores)
perc_vn = int(vn * 100 / total_eleitores)
perc_vb = int(vb * 100 / total_eleitores)

print(total_eleitores, perc_a, perc_b, perc_c, perc_vn, perc_vb)
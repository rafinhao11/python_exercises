#formula distancia (distancia = tempo * velocidade)
tempo = float(input("Tempo: "))
velocidade = float(input("Velocidade: "))

distancia = tempo * velocidade

litros_usados = distancia / 12

print(tempo, velocidade, distancia, litros_usados)
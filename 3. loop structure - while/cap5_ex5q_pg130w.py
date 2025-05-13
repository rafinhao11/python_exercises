resposta = "sim"
total = 0
while resposta == "sim":
    comodo = input("Digite o cômodo: ")
    largura = float(input("Digite a largura: "))
    comprimento = float(input("Digite o comprimento: "))
    area = largura * comprimento
    total = total + area
    resposta = input("Deseja continuar? ")
print(area, total)
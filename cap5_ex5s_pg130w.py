dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = 0
while divisor <= dividendo:
    dividendo = dividendo - divisor
    quociente = quociente + 1
print(quociente)
nome = input("Nome: ")
sexo = input("Sexo: ")

if sexo == "M":
    print("Ilmo Sr.", nome)
elif sexo == "F":
    print("Ilma Sra.", nome)
else:
    print("Sexo não encontrado!")
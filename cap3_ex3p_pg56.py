#formula reajuste salarial
#salario mensal + salario mensal * reajuste / 100
salario_mensal = float(input("Salario Mensal: "))
reajuste = float(input("Reajuste: "))

salario_reajustado = salario_mensal + salario_mensal * reajuste / 100
print(salario_reajustado)
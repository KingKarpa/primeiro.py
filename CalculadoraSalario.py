# Captura e Tratamento de dados essenciais
# Horas e Valores em dinheiro podem ser "quebrados" (float)
print("A inserção de valores deve ser no formato X ou X.Y")
valorHora = float(input("Insira o valor da sua hora: "))
horasMensais = float(input("Insira o número de horas trabalhadas no mês: "))

# Definição de Taxas essenciais
taxIR = 0.11
taxINSS = 0.08
taxSindicato = 0.05

# Realizando Cálculos
salario_Bruto = valorHora * horasMensais

desconto_IR = salario_Bruto * taxIR
desconto_INSS = salario_Bruto * taxINSS
desconto_Sindicato = salario_Bruto * taxSindicato
desconto_Total = desconto_IR + desconto_INSS + desconto_Sindicato

salario_Liquido = salario_Bruto - desconto_Total

# Exibição (print) de resultados com formatação tradicional de 2 digítos
print("+ Salário Bruto : R$ {:.2f}".format(salario_Bruto))
print("- IR (11%) : R$ {:.2f}".format(desconto_IR))
print("- INSS (8%) : R$ {:.2f}".format(desconto_INSS))
print("- Sindicato (5%) : R$ {:.2f}".format(desconto_Sindicato))
print("= Salário Líquido : R$ {:.2f}".format(salario_Liquido))
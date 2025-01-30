"""
Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

salario = float(input("Digite seu salario atual:\n"))

if salario > 1250.00:
    aumento = salario + (salario * 0.10)
    valorAumento = salario * 0.10
    porcento = "10%"
else:
    aumento = salario + (salario * 0.15)
    valorAumento = salario * 0.15
    porcento = "15%"
    
print(f"O seu salário teve um aumento de {porcento} ou seja de: R$: {valorAumento} \nAgora o valor do seu salário é de: R$: {aumento:.2f}")

"""
salary = float(input("Digite seu salário: "))
perc_increase = 0.15
if salary > 1250:
    perc_increase = 0.10
incresase = salary * perc_increase
print(f"Seu aumento será de: R$ {incresase:.2f}")


"""
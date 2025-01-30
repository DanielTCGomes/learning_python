"""
Tabuada

Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário.
"""

# Recebendo os inputs do usuário
num = int(input("Digite o número para calcular a tabuada: "))
inicio = int(input("Digite o valor inicial da tabuada: "))
fim = int(input("Digite o valor final da tabuada: "))

# Inicializando o contador
contador = inicio

# Loop while para calcular a tabuada
while contador <= fim:
    resultado = num * contador
    print(f"{num} x {contador} = {resultado}")
    contador += 1

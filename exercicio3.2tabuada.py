"""
1. Tabuada
Peça ao usuário para digitar um número e exiba a tabuada desse número de 1 a 10.
"""

num1 = float(input("Digite um número\n"))


for i in range(1, 11):
    resultado = num1 * i
    print(f"{num1} x {i} = {resultado}") 
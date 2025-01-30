"""
2. Contagem de Números Pares
Peça ao usuário para digitar um número e exiba todos os números pares de 1 até esse número.
"""

num1 = float(input("Digite um número\n"))
num1 = int(num1)  # Converte o número para inteiro

for i in range(1, num1 + 1):  # Itera de 1 até o número digitado
    if i % 2 == 0:  # Verifica se o número é par
        print(i)  # Exibe o número par


    
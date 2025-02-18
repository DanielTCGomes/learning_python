"""
3. Fatorial de um Número
Peça ao usuário para digitar um número e calcule o fatorial dele utilizando um loop for.
"""

num1 = float(input("Digite um número:\n"))
num1 = int(num1)

fatorial = 1

for i in range(1, num1 + 1):
    fatorial = fatorial * i 

print(f"O fatorial de {num1} é {fatorial}")  




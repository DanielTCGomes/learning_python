"""
Fatorial de um número

3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""

# 1 - fatorial de um número 
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
    
number = int(input("Digite o número para fatorial\n")) 
print(f"O fatorial de {number} é: {factorial(number)}")
# factorial(number) o valor de number vai para num atravez da chamada no print

# 2 - soma total de um número
#  3 -> 3 + 2 + 1
def sum (num1):
    if num1 == 1:
        return 1
    else:
        return(num1 + sum(num1 - 1))

number1 = int(input("Digite o número para soma total\n"))
print(f"A soma total de {number1} é: {sum(number1)}")
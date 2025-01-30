"""
5. Sequência de Fibonacci
Peça ao usuário para informar quantos números da sequência de Fibonacci ele quer ver. Exiba os primeiros N números da sequência.
"""

num1 = int(input("Digite quantos números de Fibonacci quer ver:\n"))

fib1 = 0
fib2 = 1

if num1 >= 1:
    print(" ")
    print(fib1)  # Exibe o primeiro número (0)
if num1 >= 2:
    print(fib2)  # Exibe o segundo número (1)
    


for i in range(3, num1 + 1):  # Começa no 3, pois os dois primeiros já foram exibidos
    result = fib1 + fib2
    fib1 = fib2
    fib2 = result
    print(result)
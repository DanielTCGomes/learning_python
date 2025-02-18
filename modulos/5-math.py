import math

# 1 - Acessar o número Pi
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessar o número de Euler
print(math.e)
print(f"{math.e:.2f}")


# 3 - Arredondar Números
num1  = 10.4
print(math.ceil(num1)) # Arredonda pra cima
print(math.floor(num1)) # Arredonda pra baixo

# 4 - Fatorias de um Número
num2 = int(input("Digite um número para o fatorial\n"))
print(math.factorial(num2))

# 5 - Potência de números
print(math.pow(2,2))

# 6 - Raiz quadrada
print(math.sqrt(169))

# 7 - MDC (Máximo Divisor Comum)
mdc = math.gcd(25,100)
print(mdc)

# 8 - Logaritmo
print(math.log(10))
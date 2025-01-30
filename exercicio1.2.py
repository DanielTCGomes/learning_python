#Escreva um programa em Python que leia quatro números e calcule a média entre esses números

num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
num3 = float(input("Digite o terceiro número:\n"))
num4 = float(input("Digite o quarto número:\n"))

media = (num1 + num2  + num3 + num4) /4 

print(f"A média dos 4 números foi: {media:.2f}\n")
import random;

n1 = random.randint(0,10)
print(n1)

num = int(input("Tente adivinhar o numero gerado no intervalo de 0 a 10: "))
while (n1 != num):
    num = int(input("Errado Tente novamente: "))
    
print(f"Parabéns você adivinhou o número gerado que foi: {n1}")


num1 = float(input("Digite quantos números quer somar:\n"))
num1 = int(num1)

sum = 0
for i in range(1, num1 +1):
    num2 = float(input("Digite um número:\n"))
    sum += num2
    
print(sum)
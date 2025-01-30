# 1 - função de potência de números
power = lambda num: num ** 2

# 2 - função que verifica se o número é par
pair = lambda x: x%2==0

# 3 - função que divide um número por outro
divNum = lambda x,y : x/y

# 4 - função que inverte uma string
reverse = lambda s: s[::-1]


print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10,2))
print(divNum(7,2))
print(reverse("Função"))
print(reverse("Tecnologia"))
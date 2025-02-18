"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""

def sum(*num):
    sum_total = 1
    for n in num:
        sum_total *= n
    print(f"Soma é: {sum_total}")

sum(7)
sum(8, 7)
sum(4, 5, 9)
sum(6, 8, 3, 1)

def fat(*num1):
    sum_total1 = 1
    for n in num1:
        sum_total1 *= n
    print(f"Soma é: {sum_total1}")
#fat inverso de 5
fat(1,2,3,4,5)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
        
        
print("######Curso######")
presentation(name="Python", category="Backend", level="Iniciante")
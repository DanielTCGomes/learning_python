"""
Lista números pares e ímpares de uma lista

Escreva uma função Python para imprimir os números 
pares e ímpares em duas listas separadas para cada uma.
"""

def numparimpar(listnumeros):
    pares = []
    parcount = 0
    impares = []
    imparcount = 0
    for lista in listnumeros:
        if lista % 2 == 0:
            pares.append (lista)
            parcount +=1
        else : 
            impares.append (lista)
            imparcount +=1
    print(f"Pares: {pares} total: {parcount}\nÍmpares: {impares} total: {imparcount}")    
            
    


numparimpar([1,2,3,4,5,6,7,8,9,10]) 

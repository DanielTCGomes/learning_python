"""
Conta letras maiúsculas e minúsculas

Escreva uma função Python que receba uma string e 
conte o número de letras maiúsculas e minúsculas desta string.
"""


def contaLetra(palavra):
    maiusculas = 0
    minusculas = 0
    for char in palavra:
        if char.isupper():
            maiusculas += 1
            
        elif char.islower():
            minusculas += 1
           
    print(f"Maiúsculas: {maiusculas}, Minúsculas: {minusculas}")
        
contaLetra("Abacate")
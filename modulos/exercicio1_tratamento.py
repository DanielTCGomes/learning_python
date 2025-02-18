"""Escreva um módulo em python para tratar algumas 
strings e que possua as seguintes funcionalidades:

1 - Inverter uma string de trás pra frente.
2 - Retornar apenas letras com índice par.
3 - Retornar apenas letras com índice ímpar."""

def inversor(a):
    return a[::-1]

def letterPar(a):
    return a[::2]

def letterImpar(a):
    return a[1::2]
        
        
    
gameDescription = """
Fifa 25 é um jogo de futebol desenvolvido pela EA Sports 
e que possibilita jogar localmente ou online.
"""

gameName = "Fifa 25" 


# string[início:fim] - índice começa na posição 0 | índice final -1

# 1 - Busque  toda string a partir da primeira posição

print(gameName[0:])

# 2 - Busque toda string até a última posição

print(gameName[:7])

# 3 - Busque toda string do terceiro indice até a última posição

print(gameName[2:])

"""
string[início:fim:passo] - índice começa na posição 0 | índice final -1
passo - determina o incremento. Por padrão esse número é o 1

"""

# 4 - Busque toda a string de 2 em 2 caracteres 

print(gameName[::2])


# 5 - Busque toda a string nos índices impares

print(gameName[1::2])


# 6 - Inverter uma string

print(gameName[::-1])



# 7 - Apenas os 3 primeiros caracteres.

text = "programming"

print(text[0:3])

# 8 - Apenas os 3 últimos caracteres.

print(text[-3:])


# 9 - A string sem o primeiro e o último caracteres.

print(text[1:10])

# 10 - Apenas as letras em índices pares.

word = "Python"

print(word[::2])

# 11 - Apenas as letras em índices ímpares.

print(word[1::2])

# 12 - Apenas a palavra "love".
sentence = "I love coding"

print(sentence[2:7])

# 13 - Apenas a palavra "coding".

print(sentence[7:])

# 14 - A frase invertida.

print(sentence[::-1])
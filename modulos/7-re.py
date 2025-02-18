import re


# 1 - Índice inical e final de palavras
#O r significa que estamos trabalhando com uma string bruta (raw string) 
text = "Índice inical"
# O r significa que estamos trabalhando com uma string bruta (raw string)
match = re.search(r"Índice inical",text)
print("Índice inicial ", match.start())
print("Índice final ", match.end())

# 2 - Buscando o índice que possui o ponto \\
site = 'https://google.com'
# Sem usar a \
# match = re.search(r'.', site)
match = re.search(r'\.', site)
print(match)


# 3 - Buscando uma lista de caracteres dentro de uma frase []
padrao = "[a-m]"
resultado = re.findall(padrao, text)
print(text)
print(resultado)


# 4 - Verifica o início de uma string ^
rule = r'^A' # Strings que começam com a letra A
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f'Corresponde: {f}')
    else:
        print(f'Não corresponde: {f}')
        




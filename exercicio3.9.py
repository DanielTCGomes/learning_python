# Contar vogais
# Peça ao usuário para inserir uma palavra e conte o número de vogais (a, e, i, o, u) usando um loop for.
# sem dar a resposta



text = input("Digite uma Palavra:\n")
vogais = ['a', 'e', 'i', 'o', 'u']


sum = 0
for i in text:
    if i in vogais:
        sum +=1
    
print(sum)
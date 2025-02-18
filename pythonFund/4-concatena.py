name = input('Digite o nome do Jogo\n')
yearLaunch = int(input('Digite o ano de lançamento\n'))
gamePrice =  float(input('Digite o preço do Jogo\n'))
planIncluded = input('Está incluso no serviço mensal\n')

#Comentários usa #

#Alternativa 1

print("###Dados do Jogo###")
print("================")
# print("Nome do jogo:", name)
# print("Ano do Jogo:", yearLaunch)
# print("Preço do Jogo:", gamePrice)
# print("Está incluído no plano?", planIncluded)

#Alternativa 2
# print("Nome do Jogo", name, "\n Ano de Lançamento", yearLaunch,
#       "\n Preço do Jogo:", gamePrice, "\n Está incluso do Serviço?", planIncluded)

#Alternativa 3
print(f"Nome do Jogo: {name} \nAno de Lançamento {yearLaunch} \nPreço do Jogo {gamePrice} \nEstá incluso no Seviço? {planIncluded}")
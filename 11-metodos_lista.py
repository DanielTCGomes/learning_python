gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2","Mario Odyssey"]

# 1 - tamanho da Lista
print(len(gamesList))

# 2 - recuperar um item da Lista
print(gamesList.index("Mario Odyssey"))

# 3 - Adiciona item ao final da lista
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordena lista
gamesList.sort()
print(gamesList)

# 5 - Copia os itens de uma lista para outra
gameReset = gamesList.copy()
gameReset.remove("Star Wars")
print(gameReset)

# 6 - Remove todos os itens da lista

gamesList.clear()
print(gamesList)
gamesTuple = ("Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2")
print(gamesTuple)
print(type(gamesTuple))

# Não possibilita adicionar valores na tupla
# Não possibilita remover valores na tupla
# Não possibilita ordenar valores na tupla

# 1 - Busque os dois primeiros itens da lista
print(gamesTuple[:2])

# Busque o último item da lista
print(gamesTuple[-1])

# Busca jogos até uma posição
print(gamesTuple[:2])

# Busca jogos de uma posição em diante
print(gamesTuple[2:])

# Recupera um item da tupla pelo índice
print(gamesTuple.index("Fifa23"))
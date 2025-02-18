# 1 - Liste valores de 0 a 10 que sejam menores do que 4.
# for i in range(10):
#     if i < 4:
#         print(i)

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["Mario Odyssey", "Donkey Kong Country", "Luigi's mansion", "Kirby"]

# 2 - jogos que possuem a letra a 
gamesList = [i for i in gamesList if "a" in i]
print(gamesList)

for i in gamesList:
    if "a" in i:
        print(i)

gamesx = ["Mario Odyssey", "Donkey Kong Country", "Luigi's mansion", "Kirby"]
# 3 - jogos que eu zerei (Kyrby)
gamesx = [i for i in gamesx if i != "Kirby" ]
print(gamesx)
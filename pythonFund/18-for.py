gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]

# 1 - Iterando valores de uma Lista
for list in gamesList:
    print(list)

print("")

# 2 - Quando a condição for atendida, o loop será encerrado
for list in gamesList:
    if list == "God of War":
        break
    print(list)
    
print("")
    
# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for list in gamesList:
    if list == "Red Dead 2":
        continue
    print(list)
    
# 3 - Avaliação Jogo
gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    nota = float(input("Digite a nota do Jogo\n"))
    sum += nota
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating:.2f}")
    
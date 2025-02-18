# 1 - função para imprimir Hello World
def wellcome():
    print("Hello World")
    
wellcome()

# 2 - função para somar dois números
def soma():
    num = int(input("Digite o primeiro Número\n"))
    num2 = int(input("Digite o segundo Número\n"))
    return (num + num2)
    
print(soma())

# 3 - função para cadastrar um jogo com return
def cadastro():
    gameName = input("Digite o nome do Jogo\n")
    yearLaunch = int(input("Digite o ano de lançamento\n"))
    gamePrice = float(input("Digite o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))
    return [gameName,yearLaunch,gamePrice,noteRating]

gameData = cadastro()

print(f"O jogo cadastrado foi: {gameData[0]}\nO ano de lançamento foi: {gameData[1]}\nO jogo custa R$: {gameData[2]:.2f}\nA nota do jogo é: {gameData[3]:.2f}")


# 4 - função para cadastrar um jogo sem return
def create_game():
    name1 = input("Digite o nome do jogo \n")
    yearLaunch1 = int(input("Digite o ano de lançamento\n"))
    gamePrice1 = float(input("Digite o preço do jogo\n"))
    noteRating1 = float(input("Digite a nota de avaliação do jogo\n"))
    print(name1)
    print(yearLaunch1)
    print(gamePrice1)
    print(noteRating1)
    
create_game()

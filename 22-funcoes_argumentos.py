# 1 - Crie uma função que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(fname, lname):
    print(f"{fname} {lname}")
    
full_name("Daniel","Teixeira")

# 2 - Crie uma função que some dois números via parâmetro
def sum(a,b):
    return a + b

print(sum(1,2))

# 2 - Argumentos defaut numa Função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
    
address()
# Pode Alterar
address("Espanha")

# 4 - Avaliação media do Jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do Jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o Jogo:\n"))
        sum += note
    print(f"Media da nota do jogo {game_name} foi: {sum / qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
rating_game(rating)
team = {}
done = False

def addTeam():
    teamName = input("Digite o Nome do seu Time: ")
    if teamName not in team:
        print("")
        team[teamName] = {"name" : teamName, "Players": [] }
        print(f"O time {teamName}, foi adicionado!")
    else:
        print(f"O time '{teamName}' já existe!")
    
    
def listTeam():
    if len(team) > 0:
        for i, teamValues in enumerate(team.values(), start=1):
            print(f"{i}: {teamValues['name']} ({len(teamValues['Players'])} jogadores)")
    else:
        print("Você ainda não adicionou um time!")
    
def listPlayers():
    listTeam()
    print("")
    if len(team) > 0:
        try:
            teamId = int(input("Digite o Numero do Time que Deseja Listar os Jogadores: "))
            print("")
            if teamId >= 1 and teamId <= len(team):
                teamName =  list(team.keys())[teamId - 1]
                if len(team[teamName]["Players"]) > 0:
                    for i, playerWithId in enumerate(team[teamName]["Players"],start=1):
                        print(f"{i} : {playerWithId}")
                else:
                    print(f"Você não adicionou jogadores ao time {teamName}.")
            else:
                print("")
                print("ID inválido! O time não foi encontrado.\n")
        except ValueError:
            print("")
            print("Número Invalido\n")
    else:
        print("Você ainda não adicionou um Time!")
    
def addPlayers():
    if len(team) > 0:
        listTeam()
        print("")
        try:
            teamId = int(input("Digite o Numero do Time que Deseja adicionar um Jogador: "))
            print("")
            if 1 <= teamId <= len(team):
                lista = list(team.keys())
                teamName = lista[teamId - 1]
                print(f"Você Escolheu o Time: {teamName}")
                print("")
                playerName = (input("Digite o Nome do Jogador : "))
                team[teamName]["Players"].append(playerName)
                print(f"\nO Jogador {playerName} foi adicionado ao Time: {teamName}")
            else:
                print("\nNúmero Inválido\n")
        
        except ValueError:
            print("")
            print("Número Invalido\n")

def removeTeam():
    if len(team) > 0:
        listTeam()
        print("")
        try:
            teamId = int(input("Digite o Id do Time que Deseja remover: "))
            if teamId >= 1 and teamId <= len(team):
                teamName = list(team.keys())[teamId -1]
                print(f"O {teamName} foi removido!\n")
                del team[teamName]
            else:
                print("")
                print("ID inválido! O time não foi encontrado.\n")
        except ValueError:
            print("Entrada inválida! Digite um número válido.\n")
    else:
        print("")
        print("Você ainda não adicionou um Time!")
        
        
def removePlayers():
    if len(team) > 0 :
        listTeam()
        print("")
        try:
            teamId = int(input("Digite o Id do Time que Deseja Remover um Jogador: ")) 
            print("")
            if 1 <= teamId <= len(team):
                teamName =  list(team.keys())[teamId - 1]
                if len(team[teamName]["Players"]) > 0 :
                    removePlayer = input("Digite o nome do Jogador que Deseja Remover: ")
                    print("")
                    if removePlayer in  team[teamName]["Players"]:
                        team[teamName]["Players"].remove(removePlayer)
                        print(f"Jogador {removePlayer} foi removido\n")
                        
                    else:
                        print("Nome do Jogador Não Corresponde ao que está na Lista\n")
                     
                else:
                    print("Você ainda não adicionou Jogadores a um time")
            else:
                print("Número Inválido")
        except ValueError:
            print("Entrada inválida! Digite um número válido.\n")
    else:
        print("Você ainda não adicionou um time")
                
while not done:
    print("")
    print("1: Adicionar Times")
    print("2: Listar Times")
    print("3: Remover um Time")
    print("4: Adicionar Jogadores")
    print("5: Remover um Jogador")
    print("6: Listar Jogadores")
    print("7: Sair")
    print("")
    try:
        choice = int(input("Digite o Número da Opção que Deseja: "))
        if 1 <= choice <= 7:
            print("")
            if choice == 1:
                addTeam()
            elif choice == 2:
                listTeam()
            elif choice == 3:
                removeTeam()
            elif choice == 4:
                addPlayers()
            elif choice == 5:
                removePlayers()
            elif choice == 6:
                listPlayers()
            elif choice == 7:
                done = True
        else:
            print("Digite um número relacionado a umas das Opções \n")
    
    except ValueError:
        print("\nNúmero Inválido. Digite um número entre 1 e 7.\n")

    
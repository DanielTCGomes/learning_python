def addTeam():
    teamName = input("Digite o nome do seu time: ")
    print("")
    return teamName

def addPlayers():
    players = input("Adicione um Jogador ao seu time: ")
    return players


option = 0
teamNames = {}  

while option != 7:
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Listar Times")
    print("3. Adicionar Jogador a um time")
    print("4. Listar Jogadores de um Time")
    print("7. Sair")
    option = int(input("Digite uma das opções: "))
    print("")
    
    if option == 1:
        teamId = len(teamNames) + 1  # Cria um identificador único para o time
        teamName = addTeam()
        teamNames[teamId] = {"name": teamName, "players":[]}  # Adiciona ao dicionário com o ID como chave
        print(f"Time adicionado: ID={teamId}, Nome={teamName}\n")
    elif option == 2:
        if teamNames:
            print("Times adicionados:")
            for teamId, name in teamNames.items():
                print(f"ID: {teamId}, Nome: {name}")
            print("")
        else:
            print("Nenhum time foi adicionado ainda.\n")
    elif option == 3:
        if teamNames:
            print("Selecione o time ao qual deseja adicionar um jogador:")
            for teamId, teamInfo in teamNames.items():
                print(f"ID: {teamId}, Nome: {teamInfo['name']}")
            num = int(input("Digite o ID do time: "))
            
            if num in teamNames:
                player = addPlayers()
                teamNames[num]['players'].append(player)  # Adiciona o jogador à lista de jogadores do time
                print(f"Jogador '{player}' adicionado ao time '{teamNames[num]['name']}'.\n")
            else:
                print("ID do time inválido. Tente novamente.\n")
        else:
            print("Nenhum time foi adicionado ainda. Por favor, adicione um time primeiro.\n")
    elif option == 4:
        if teamNames:  # Verifica se existem times cadastrados
            print("Selecione o time ao qual deseja listar os jogadores:")
            for teamId, teamInfo in teamNames.items():
                print(f"ID: {teamId}, Nome: {teamInfo['name']}")
            num = int(input("Digite o ID do time: "))
            if num in teamNames:  # Verifica se o ID do time existe
                if len(teamNames[num]['players']) == 0:  # Verifica se a lista está vazia
                    print(f"O time '{teamNames[num]['name']}' ainda não possui jogadores cadastrados.\n")
                else:
                    players = teamNames[num]['players']
                    print(f"Jogadores do time '{teamNames[num]['name']}': {', '.join(players)}\n")
            else:
                print("ID do time inválido. Tente novamente.\n")
        else:
            print("Nenhum time foi adicionado ainda. Por favor, adicione um time primeiro.\n")


             


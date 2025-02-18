import webbrowser

done = False

while not done:
    print("O que você deseja fazer?")
    print("1. Aprender Phyton")
    print("2. Aprender sobre módulos")
    print("3. Aprender Python, Fullstack Js, Ingles e No Code")
    print("4. Sair")
    
    choice = input("Digite umas das Opções: ")
    
    if choice == "1":
        webbrowser.open("http://www.python.org")
    elif choice == "2":
        webbrowser.open("https://docs.python.org/3/2")
    elif choice == "3":
        webbrowser.open("https://www.google.com")
    elif choice == "4":
            done = True
    else:
        print("Opção inválida. Escolha uma opção entre 1 a 4")
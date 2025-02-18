"""
Crie um programa que peça para o usuário preencher
o conteúdo de uma matriz de dimensões 3x4. Após
inseridos os dados, realize uma busca na matriz e
informe quais são os valores das linhas e colunas
(posição) do maior e do menor elemento de toda a
matriz.

"""
# Inicializando a matriz 3x4 com zeros
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
   

# Preenchendo a matriz com valores do usuário
for i in range(3):
    print(f"Linhas{i}")# Percorre as linhas
    for j in range(4):  # Percorre as colunas
        matriz[i][j] = int(input(f"Digite um valor para a posição [{i},{j}]: "))
        
maior = matriz[0][0]
menor = matriz[0][0]          

        
for i in range(3):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            
print(f"\nO Maior número da matriz foi:{maior}")
print(f"\nO menor número da matriz foi:{menor}")

# Exibindo a matriz preenchida
print("\nMatriz preenchida:")
for linha in matriz:
    print(linha)
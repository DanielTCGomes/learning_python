"""
Cálculo da Distância

Escreva um programa que pergunte a distância que um 
passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km 
para viagens de até de 200 km, 
e R$ 0,35 para viagens mais longas.
"""

distancia = float(input("Quantos Km você deseja percorrer\n"))
if distancia <= 200:
    valorPassagem = distancia * 0.50
else:
    valorPassagem = distancia * 0.30

print(f"O valor da sua passagem ficou no valor de: R$: {valorPassagem:.2f}")
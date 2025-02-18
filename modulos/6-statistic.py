import statistics

# 1 - Aplicar a média
print(statistics.mean([3,2,5,8,9]))
print(statistics.mean([3,2,5,6,9]))

# 2 - Aplicar a mediana
#Encontrar o Valor Central
print(statistics.median([1, 2, 3, 8, 9]))
# No Caso de Pares a gente agrupa os dois 
# centrais Soma e Divide por 2
print(statistics.median([1, 2, 3, 7, 8, 9]))

# 3 - Aplicar a moda
# Achar o Número que mais se Repete
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4 ,2 ,5 ,6]))

# 4 - Desvio padrão
"""
- Quanto mais próximo de 0 for o desvio padrão,
significa que os dados do conjunto estão menos dispersos

O desvio padrão é usado para medir o 
quanto os dados variam em relação à média. Ele é muito 
útil em diversas áreas da vida real. Aqui estão 
alguns exemplos:

Notas de alunos em uma escola
Se uma prova tem média 70 pontos, mas um desvio padrão alto, significa que há muitas notas muito baixas e muito altas (grande variação). Já um desvio padrão baixo indica que a maioria dos alunos tirou notas próximas da média.

✅ Baixo desvio padrão → Notas próximas da média.
⚠️ Alto desvio padrão → Notas muito dispersas.

"""

print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))
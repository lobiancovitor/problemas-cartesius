# Data: 20/05/2024
# Inicio: 9:57
# Fim: 10:19

# Enunciado no fim do arquivo

"""
O programa deve armazenar a média dos pesos dos camelos

Como distribuir o peso?

Se peso_camelo > média => subtrair a diferença entre o peso do camelo e a média de todos os camelos
Se peso_camelo < média => adicionar a diferença entre o peso do camelo e a média de todos os camelos
"""

n = int(input())

pi = []

for i in range(n):
    peso = int(input())

    pi.append(peso)

peso_total = sum(pi)  # Armazena a soma dos pesos

media_peso = peso_total / len(pi)  # Armazenar a média dos pesos dos camelos

for i, p in enumerate(
    pi
):  # Percorrer a lista e fazer comparações entre o peso de um camelo e a média de todos
    if p > media_peso:
        print(f"-{p - media_peso}")
    else:
        print(media_peso - p)

# Printa conforme a distribuição dos pesos entre os camelos


"""
No deserto da Nlogônia, uma longa caravana de camelos carregados de especiarias está parada num oásis para descansar. O chefe da caravana notou que alguns camelos pareciam mais cansados do que os outros, e descobriu que cada camelo estava carregando um peso diferente, de forma que alguns camelos carregam um peso muito maior do que outros e portanto se cansam mais. Aproveitando a parada para descanso, o chefe da caravana quer redistribuir as especiarias entre os camelos, de forma que todos os camelos carreguem exatamente o mesmo peso. Dados os pesos carregados por cada camelo antes da parada, escreva um programa que determine, para cada camelo, qual o peso que deve ser retirado ou adicionado, para que todos carreguem exatamente o mesmo peso.

Entrada
A primeira linha contém um inteiro N, o número de camelos na caravana. Os camelos são numerados de 1 a N. Cada uma das linhas seguintes contém um inteiro Pi , o peso que o camelo de número i carregava antes da parada. Os camelos são dados em ordem crescente de numeração.

Saída
Para cada camelo da caravana, seu programa deve produzir uma linha, o valor que deve ser adicionado ou retirado desse camelo para que todos os camelos carreguem o mesmo peso. A ordem dos camelos na saída deve ser a mesma ordem dada na entrada. Para todos os casos de teste o peso que cada camelo deve carregar é um número inteiro.

Restrições • 1 ≤ N ≤ 1 000 • 1 ≤ Pi ≤ 10 000 para 1 ≤ i ≤ N
"""

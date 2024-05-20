# Inicio: 9:57
# Fim: 10:19

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

peso_total = sum(pi) # Armazena a soma dos pesos

media_peso = peso_total / len(pi) # Armazenar a média dos pesos dos camelos

for i, p in enumerate(pi): # Percorrer a lista e fazer comparações entre o peso de um camelo e a média de todos
    if p > media_peso:
        print(f"-{p - media_peso}")
    else:
        print(media_peso - p)

# Printa conforme a distribuição dos pesos entre os camelos
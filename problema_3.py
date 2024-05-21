# Data: 21/05/2024
# Inicio: 10:59
# Fim: -

# Enunciado no fim do arquivo

"""

N = 1 => 1
N = 2 => -1 (inválido: média nunca vai estar na linha / coluna)

N = par?

N = impar => basta inserir os valores de forma crescente na matriz. 
A média sempre será o valor do meio (para linha e coluna)

3 <= N <= 40

-> Matriz[N][N] ou Matriz[i][j], com valores inseridos de forma crescente

Inserir valores de forma crescente garante que não serão repetidos.

-> Rebalanceamento?
Como rebalancear linhas e colunas ao mesmo tempo?

-> Restrição: A soma dos números da linha ou coluna / N deve ser inteiro
===============================================
Exemplo com N = 4: 

Opção 1:
[1 2 3 4] => soma = 10 => 10/4 = 2.5
Opção 2:
[1 2 3 5] => soma = 11 => 11/4 = 2.75 => com N par, a soma nunca pode ser impar
Opção 3:
[1 2 3 6] => soma = 12 => 12/4 = 3 => inteiro e está presente na linha. OK

?? Distância entre [3 6] = N-1

Opção 1:
[7 8 9 10] => soma = 34 => 34/4 = 8.5
Opção 2:
[7 8 9 11] => soma = 35 => 35/4 = 8.75
Opção 3:
[7 8 9 12] => soma = 36 => 36/4 = 9 => inteiro e está presente na linha. OK

?? Distância entre [9 12] = N-1

===============================================
Exemplo com N = 5:

Opção 1:
[1 2 3 4 5] => soma = 15 => 15/5 = 3 => inteiro e está presente na linha. OK
[6 7 8 9 10] => soma = 40 => 40/5 = 8 => inteiro e está presente na linha. OK
[11 12 13 14 15] => soma = 65 => 65/5 = 13 => inteiro e está presente na linha. OK
[16 17 18 19 20] => soma = 90 => 90/5 = 18 => inteiro e está presente na linha. OK
[21 22 23 24 25] => soma = 115 => 115/5 = 23 => inteiro e está presente na linha. OK

?? Quando N é impar, não precisar rebalancear e a média sempre será o valor do meio (para linha e coluna)

=> Ou seja, para N ímpar, basta inserir os valores de forma crescente na matriz
"""


















"""

Um quadrado fantástico é um conjunto de números inteiros positivos dispostos em N linhas por N colunas, tal que: • Não há números repetidos no quadrado. • A média dos números em cada linha é um número inteiro que está presente na linha. • A média dos números em cada coluna é um número inteiro que está presente na coluna.

Entrada

A primeira e única linha da entrada contém um número inteiro N, indicando a dimensão do quadrado.

Saída

Seu programa deve produzir N linhas, cada uma contendo N números inteiros Xi , representando um quadrado fantástico.

Restrições • 1 ≤ N ≤ 40 • 1 ≤ Xi ≤ 1000000

Informações sobre a pontuação • Para um conjunto de casos de testes valendo 44 pontos, 1 ≤ N é ímpar. • Para outro conjunto de casos de testes valendo 56 pontos, nenhuma restrição adicional.

Exemplo de entrada

1

Exemplo de saída

1

"""


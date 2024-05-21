# Data: 21/05/2024
# Inicio: 10:59
# Fim: 12:16

# Enunciado no fim do arquivo

"""
============ RESPOSTA ============
N = 1 => 1
N = 2 => -1 (inválido: média nunca vai estar na linha / coluna)

N = impar => basta inserir os valores de forma crescente na matriz.
A média sempre será o valor do meio (para linha e coluna)

RESOLUÇÃO PARA N PAR, MAIOR QUE 2:
-> Rebalancear o último número de cada linha até que a média da soma da linha seja encontrada na mesma linha
-> Com os 2 exemplos: Para N=4, o último da linha = penúltimo + (N-1). Com N=6, penúltimo + (N-2)...
-> Rebalancear o primeiro número da última linha até que a média da soma da coluna seja encontrada na mesma
-> Após rebalancear, os números seguintes continuam em ordem crescente (soma-se 1)

=> O rebalanceamento sempre será na ultima linha e na última coluna
============ RESPOSTA ============
"""


"""
============ INÍCIO RESOLUÇÃO ============

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
[1 2 3 6] => soma = 12 => 12/4 = 3 => inteiro e está presente na linha. OK [3 6] = N - 1

Opção 1:
[7 8 9 10] => soma = 34 => 34/4 = 8.5
Opção 2:
[7 8 9 11] => soma = 35 => 35/4 = 8.75
Opção 3:
[7 8 9 12] => soma = 36 => 36/4 = 9 => inteiro e está presente na linha. OK [9 12] = N - 1

===============================================
Exemplo com N = 6:

[1  2  3  4  5   9] => soma = 24 => 24/6 = 4. OK [5 9] = N - 2
[10 11 12 13 14 18] => soma = 78 => 78/6 = 13. OK [14 18] = N - 2
[19 20 21 22 23 27] => soma = 132 => 132/6 = 22. OK [23 27] = N - 2
[28 29 30 31 32 36] => soma = 186 => 186/6 = 31. OK [32 36] = N - 2
[37 38 39 40 41 45] => soma = 240 => 240/6 = 40. OK [41 45] = N - 2
[73 74 75 76 77 81] => soma = 456 => 456/6 = 76. OK [77 81] = N - 2

46 -> 47 = 142 Nao
47 -> 48 = 143 Nao
48 -> 49 = 144 Nao
49 -> 73 = 168 Sim => 168/6 = 28 -> Ou seja, rebalanceando a primeira coluna, 46 vai para 73 e seguimos crescente

RESOLUÇÃO PARA N PAR, MAIOR QUE 2:
-> Rebalancear o último número de cada linha até que a média da soma da linha seja encontrada na mesma linha
-> ? Para N=4, o último da linha = penúltimo + (N-1). Com N=6, penúltimo + (N-2)...
-> Rebalancear o primeiro número da última linha até que a média da soma da coluna seja encontrada na mesma
-> Após rebalancear, os números seguintes continuam em ordem crescente (soma-se 1) 

=> O rebalanceamento sempre será na ultima linha e na última coluna
===============================================
Exemplo com N = 5:

Opção 1:
[1 2 3 4 5] => soma = 15 => 15/5 = 3 => inteiro e está presente na linha. OK
[6 7 8 9 10] => soma = 40 => 40/5 = 8 => inteiro e está presente na linha. OK
[11 12 13 14 15] => soma = 65 => 65/5 = 13 => inteiro e está presente na linha. OK
[16 17 18 19 20] => soma = 90 => 90/5 = 18 => inteiro e está presente na linha. OK
[21 22 23 24 25] => soma = 115 => 115/5 = 23 => inteiro e está presente na linha. OK

Quando N é impar, não precisar rebalancear e a média sempre será o valor do meio (para linha e coluna)

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

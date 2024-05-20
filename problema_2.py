# Data: 20/05/2024
# Inicio: 10:59
# Fim: 11:53

# Enunciado no fim do arquivo

"""

Lógica:
Separar o número inicial A. A quantidade de digitos possíveis deve ser <= inteiro truncado de (tamanho da lista)/2

Exemplo:
5 digitos -> número com maior quantidade de dígitos terá 2 digitos
8 digitos -> número com maior quantidade de dígitos terá 4 digitos

De acordo com a quantidade de dígitos de cada A, ver se os números seguintes estão em sequencia ou não.

Se não estiverem em sequencia, não está ordenado. Portanto, elimina-se aquele A.

Caso estiver em sequencia, esse A será válido.

O primeiro A válido será sempre o menor A possível, tendo em vista a quantidade de dígitos dos seguintes.

Portanto, ao achar o primeiro A válido, temos a resposta para o menor valor possível de A.

============================================

Exemplo com 9 digitos [ 1 9 9 2 0 0 2 0 1 ]

A possíveis:

A1 = 1
A2 = 19
A3 = 199
A4 = 1992   => acaba aqui pois 9/2 = 4.5 (máximo de 4 dígitos)

Para cada possibilidade de A, ver se os próximos números seguem na ordem (>=).

Exemplo:

A1 -> 1 - 9 - 9 - 2      => não está ordenado. A1 eliminado.
A2 -> 19 - 92 - 00       => não está ordenado. A2 eliminado.
A3 -> 199 - 200 - 201    => está ordenado e A3 é o menor A possível, os demais serão sempre maiores que A3.

============================================

Exemplo com 6 digitos [ 1 2 3 1 2 4 ]

A possíveis:

A1 = 1
A2 = 12
A3 = 123   => acaba aqui pois 6/2 = 3 (máximo de 3 dígitos)

Para cada possibilidade de A, ver se os próximos números seguem na ordem (>=).

Exemplo:

A1 -> 1 - 2 - 3 - 1      => não está ordenado. A1 eliminado.
A2 -> 12 - 31 - 24       => não está ordenado. A2 eliminado.
A3 -> 123 - 124          => está ordenado e A3 é o menor A possível, os demais serão sempre maiores que A3.

============================================

Exemplo com 5 digitos [ 9 1 0 1 1 ]

A possíveis:

A1 = 9
A2 = 91    => acaba aqui pois 5/2 = 2.5 (máximo de 2 dígitos)

Para cada possibilidade de A, ver se os próximos números seguem na ordem (>=).

Exemplo:

A1 -> 9 - 10 - 11        => está ordenado e A1 é o menor A possível, os demais serão sempre maiores que A1.
A2 -> 91 - 01            => não está ordenado. A2 eliminado.

"""

"""
Joãozinho te propôs o seguinte desafio: ele escolheu dois inteiros A e B, com 1 ≤ A ≤ B ≤ 101000, e escreveu na lousa todos os inteiros entre A e B, em sequência, porém colocando um espaço após cada dígito, de forma a não ser possível ver quando um número termina ou começa. Por exemplo, se Joãozinho escolher A = 98 e B = 102, ele escreveria a sequência “9 8 9 9 1 0 0 1 0 1 1 0 2”. Seu desafio é: dada a lista de dígitos escritos na lousa, encontrar os valores de A e B. Caso exista mais de uma possibilidade para os valores que geraria a lista, você deve encontrar uma em que o valor de A é o menor possível. É garantido que a lista de dígitos da lousa tem no máximo tamanho 1000.

Entrada
A primeira linha da entrada contém um único inteiro N, indicando o número de dígitos. A segunda linha contém N inteiros di, indicando os dígitos escritos.

Saída
Imprima o menor valor possível de A. Restrições • 1 ≤ N ≤ 1000 • 0 ≤ di ≤ 9 Informações sobre a pontuação • Para um conjunto de casos de testes valendo 21 pontos, 1000 ≤ A ≤ B ≤ 9999. • Para outro conjunto de casos de testes valendo 23 pontos, B = A + 1. • Para outro conjunto de casos de testes valendo 40 pontos, A, B < 106 . • Para outro conjunto de casos de testes valendo 16 pontos, nenhuma restrição adicional.
"""

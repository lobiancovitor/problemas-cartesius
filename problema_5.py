# Data: 20/05/2024
# Inicio: 10:33
# Fim: 10:51
# Revisões: 1

# Eu tinha feito divindo por mult=33 ao invés de multiplicar para achar o número

# Enunciado no fim do arquivo

mult = 33


def sum_digits(n: int) -> int:
    """Retorna a soma dos algarismos de um número"""
    soma = sum(int(i) for i in str(n))

    return soma


def search_seven(n: int) -> bool:
    """Checa se n possui todos algarismos iguais a 7"""
    for i, v in enumerate(str(n)):
        if v != "7":
            return False
    return True


# número satisfatório = o menor número inteiro positivo que multiplicado por 33 resulta em um número cujos algarismos são todos iguais a 7

i = 1
# Atualmente -> O(N²) -> Melhorar
while True:
    m = mult * i
    if search_seven(m):  # Multiplicando 33 por i até achar um i com todos algarismos 7
        print(sum_digits(i))  # Printando a soma dos algarismos de i
        break
    else:
        i += 1


"""
Seja N o menor número inteiro positivo que multiplicado por 33 resulta em um número cujos algarismos são todos iguais a 7. Determine a soma dos algarismos de N.
"""

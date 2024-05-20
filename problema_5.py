# Data: 20/05/2024
# Inicio: 10:33
# Fim: 10:51

# Enunciado no fim do arquivo

start = "777"  # Começar com o menor número possível com algarismos 7

# start é uma string para que possamos adicionar mais 7 conforme necessário

mult = 33


def sum_digits(n: int) -> int:
    """Retorna a soma dos algarismos de um número"""
    soma = sum(int(i) for i in str(n))

    return soma


# número satisfatório = o menor número inteiro positivo que multiplicado por 33 resulta em um número cujos algarismos são todos iguais a 7

while True:  # Enquanto não achar um número satisfatório
    n = int(start) % mult
    if isinstance(n, int):  # Deve ser um valor inteiro
        print(
            sum_digits(n)
        )  # Printa a soma dos algarismos do primeiro número satisfatório
        break
    else:
        start + "7"  # Concatenar 7 em start conforme necessário


"""
Seja N o menor número inteiro positivo que multiplicado por 33 resulta em um número cujos algarismos são todos iguais a 7. Determine a soma dos algarismos de N.
"""

from tools_vetor import criar_vetor

def main():
    qtd = int(input('Quantos elementos terão os vetores? '))

    print('Vetor A:')
    vetor_a = criar_vetor(qtd)
    print('Vetor B:')
    vetor_b = criar_vetor(qtd)

    vetor_c = somar_vetores(vetor_a, vetor_b)

    print(vetor_c)


def somar_vetores(vetor1, vetor2):
    vetor3 = vetor1 + vetor2
    return vetor3


main()

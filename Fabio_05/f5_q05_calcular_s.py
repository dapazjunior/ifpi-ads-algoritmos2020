from tools_vetor import criar_vetor_num

def main():
    print('Vetor(20 elementos):')
    vetor = criar_vetor_num(20)

    soma = calcular_s(vetor)
    print(f'S = {soma}')


def calcular_s(vetor):
    inicio = 0
    final = len(vetor) - 1
    soma = 0

    while inicio < 10:
        soma_parcial = (vetor[inicio] - vetor[final]) ** 2
        soma += soma_parcial

        inicio += 1
        final -= 1

    return soma


main()

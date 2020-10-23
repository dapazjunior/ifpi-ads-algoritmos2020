from tools_vetor import criar_vetor

def main():
    qtd = int(input('Quantos elementos terão os vetores? '))

    print('Vetor A:')
    vetor_a = criar_vetor(qtd)
    print('Vetor B:')
    vetor_b = criar_vetor(qtd)

    intercecao = vetor_intercecao(vetor_a, vetor_b)
    uniao = vetor_uniao(vetor_a, vetor_b)

    print(f'Intercessão: {intercecao}')
    print(f'União: {uniao}')


def vetor_intercecao(vetor1, vetor2):
    vetor = []

    for i in vetor1:
        if i in vetor2:
            vetor.append(i)
    

    return vetor


def vetor_uniao(vetor1, vetor2):
    vetor = vetor1

    for i in vetor2:
        if i not in vetor:
            vetor.append(i)
    
    vetor.sort()

    return vetor


main()

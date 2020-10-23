from tools_vetor import criar_vetor

def main():
    qtd = int(input('VETOR A:\nQuantos elementos? '))

    vetor_a = criar_vetor(qtd)
    vetor_b = inverter_vetor(vetor_a)

    print(f'Vetor A: {vetor_a}')
    print(f'Vetor B: {vetor_b}')


def inverter_vetor(vetor):
    novo_vetor = []
    limite = len(vetor) - 1

    while limite >= 0:
        novo_vetor.append(vetor[limite])
        limite -= 1
    
    return novo_vetor

main()

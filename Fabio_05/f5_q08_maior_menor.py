from tools_vetor import criar_vetor_num

def main():
    qtd = int(input('Digite a quantidade de elementos: '))
    vetor = criar_vetor_num(qtd)

    print(f'Vetor: {vetor}\n')

    maior, posicao_maior = verificar_maior(vetor)
    print(f'Maior: {maior}')
    print(f'Posição: {posicao_maior}')

    menor, posicao_menor = verificar_menor(vetor)
    print(f'\nMenor: {menor}')
    print(f'Posição: {posicao_menor}')


def verificar_maior(vetor):
    maior = vetor[0]
    pos = 0
    pos_maior = 0

    for num in vetor:
        if num > maior:
            maior = num
            pos_maior = pos
        
        pos += 1
    
    return maior, pos_maior


def verificar_menor(vetor):
    menor = vetor[0]
    pos = 0
    pos_menor = 0

    for num in vetor:
        if num < menor:
            menor = num
            pos_menor = pos
        
        pos += 1
    
    return menor, pos_menor


main()

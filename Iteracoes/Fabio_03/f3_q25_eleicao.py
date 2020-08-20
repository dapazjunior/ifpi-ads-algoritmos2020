def main():
    n = int(input('Quantos eleitores votarão? '))

    votos1 = 0
    votos2 = 0
    votos3 = 0
    votos_nulo = 0
    votos_branco = 0
    
    contador_eleitores = 1

    while contador_eleitores <= n:
        print(f'Pessoa {contador_eleitores}')
        voto = int(input('Digite seu voto: '))

        if voto == 1:
            votos1 += 1
        elif voto == 2:
            votos2 += 1
        elif voto == 3:
            votos3 += 1
        elif voto == 0:
            votos_branco += 1
        else:
            votos_nulo += 1
        
        contador_eleitores += 1
    
    print(f'Candidato 1: {votos1} votos')
    print(f'Candidato 2: {votos2} votos')
    print(f'Candidato 3: {votos3} votos')
    print(f'Brancos: {votos_branco} votos')
    print(f'Nulos: {votos_nulo} votos\n')
    
    quem_venceu(votos1, votos2, votos3)


def quem_venceu(votos1, votos2, votos3):
    if votos1 > votos2 and votos1 > votos3:
        print('Vencedor: Candidato 1')
    elif votos2 > votos1 and votos2 > votos3:
        print('Vencedor: Candidato 2')
    elif votos3 > votos1 and votos3 > votos2:
        print('Vencedor: Candidato 3')
    elif votos1 == votos2 and votos1 > votos3:
        print('Empate: Candidatos 1 e 2')
    elif votos1 == votos3 and votos1 > votos2:
        print('Empate: Candidatos 1 e 3')
    elif votos2 == votos3 and votos1 > votos3:
        print('Empate: Candidatos 2 e 3')
    else:
        print('Empate: Candidatos 1, 2 e 3')


main()

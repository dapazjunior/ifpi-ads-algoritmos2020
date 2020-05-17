def main():
    total_votos = 0
    serra = 0
    dilma = 0
    ciro = 0
    indeciso = 0
    outros = 0
    nulo_branco = 0

    while True:
        voto = int(input('Qual a sua inteção de voto? '))

        if voto == -1:
            break
        if voto == 45:
            serra += 1
        if voto == 13:
            dilma += 1
        if voto == 23:
            ciro += 1
        if voto == 99:
            indeciso += 1
        if voto == 98:
            outros += 1
        if voto == 0:
            nulo_branco += 1
        
        total_votos += 1
    
    serra = serra / total_votos * 100
    dilma = dilma / total_votos * 100
    ciro = ciro / total_votos * 100
    indeciso = indeciso / total_votos * 100
    outros = outros / total_votos * 100
    nulo_branco = nulo_branco / total_votos * 100
    

    print('>>> RESULTADO DA PESQUISA <<<')
    print(f'SERRA: {serra:.1f} %')
    print(f'DILMA: {dilma:.1f} %')
    print(f'CIRO: {ciro:.1f} %')
    print(f'INDECISOS: {indeciso:.1f} %')
    print(f'OUTROS: {outros:.1f} %')
    print(f'BRANCOS E NULOS: {nulo_branco:.1f} %')


main()

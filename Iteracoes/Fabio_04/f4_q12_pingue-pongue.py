def main():
    pontos_1 = 0
    pontos_2 = 0

    condicao = False

    while not condicao:
        if condicao:
            break

        ponto = int(input('Ponto para 1 ou 2? '))

        if ponto == 1:
            pontos_1 += 1
        if ponto == 2:
            pontos_2 += 1
        print(f'Placar: {pontos_1} x {pontos_2}')
        
        condicao = ((pontos_1 >= 21) or (pontos_2 >= 21)) and ((pontos_1 - pontos_2 >= 2) or (pontos_2 - pontos_1 >= 2))
    
    if pontos_1 > pontos_2:
        print(f'O jogador 1 venceu por {pontos_1} x {pontos_2}')
    
    if pontos_2 > pontos_1:
        print(f'O jogador 2 venceu por {pontos_2} x {pontos_1}')


main()

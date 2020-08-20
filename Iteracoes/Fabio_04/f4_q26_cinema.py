def main():
    idade_otimo = 0
    qtd_otimo = 0
    qtd_regular = 0
    qtd_bom = 0
    qtd_total = 0
    
    while True:
        idade = int(input('Idade: '))
        if idade == -1:
            break
        
        opiniao = int(input('Opinião: '))
        if opiniao == 1:
            idade_otimo += idade
            qtd_otimo += 1
        
        elif opiniao == 2:
            qtd_bom += 1
        
        elif opiniao == 3:
            qtd_regular += 1
        
        qtd_total += 1
    
    media_otimo = idade_otimo / qtd_otimo
    percent_bom = qtd_bom / qtd_total * 100
    
    print(f'\nMedia das idades dos que acahram Ótimo: {media_otimo:.1f} anos.')
    print(f'Quantidade de pessoas que respondeu Regular: {qtd_regular} pessoas.')
    print(f'Percentual das pessoas que respondeu Bom: {percent_bom}% das pessoas')


main()

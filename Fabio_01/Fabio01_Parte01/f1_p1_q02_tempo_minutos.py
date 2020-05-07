def main():
    '''Lê um valor em horas e um valor em minutos.
    O valor em horas é convertido em minutos e depois somado com o valor em minutos fornecido.
    
    Retorna o valor total em minutos'''
    
    horas = int(input('Digite um valor em horas: '))
    minutos_parcial = int(input('Digite um valor em minutos: '))
    
    minutos_total = calcular_minutos(horas, minutos_parcial)
    
    print(f'O valor é {minutos_total} minutos')


def calcular_minutos(horas, minutos_parcial):
    h_em_min = horas * 60
    
    minutos_total = h_em_min + minutos_parcial
    
    return minutos_total


main()

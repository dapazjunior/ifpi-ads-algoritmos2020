def main():
    '''Recebe um valor em minutos e retorna o valor em horas e minutos.
    O valor em horas é refente ao número máximo de horas inteiras no valor de minutos de entrada.
    O valor em minutos é referente aos minutos que sobram das horas calculadas.'''
    
    minutos_entrada = int(input('Digite um valor em minutos: '))
    
    horas = calcular_horas(minutos_entrada)
    minutos_saida = calcular_minutos(minutos_entrada)
    
    print(f'O resultado é {horas} horas e {minutos_saida} minutos')


def calcular_horas(minutos_entrada):
    '''Divide o valor de minutos de entrada por 60, resultando num valor inteiro de horas.
    Retorna o valor de horas.'''
    
    horas = minutos_entrada // 60
    return horas

def calcular_minutos(minutos_entrada):
    '''Calcula o resto da divisão de minutos de entrada por 60, resultando nos minutos restantes.
    Retorna o valor em minutos restantes.'''
    
    minutos_saida = minutos_entrada % 60
    return minutos_saida


main()

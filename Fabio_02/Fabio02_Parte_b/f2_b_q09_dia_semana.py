def main():
    dia = int(input('Digite o número do dia da semana: '))
    
    dia = verificar_dia(dia)
    
    if dia == 'Valor Inválido!':
        print(dia)
        main()
    else:
        print(dia)

def verificar_dia(dia):
    if dia == 1:
        return 'Domingo'
    elif dia == 2:
        return 'Segunda'
    elif dia == 3:
        return 'Terça'
    elif dia == 4:
        return 'Quarta'
    elif dia == 5:
        return 'Quinta'
    elif dia == 6:
        return 'Sexta'
    elif dia == 7:
        return 'Sábado'
    else:
        return 'Valor Inválido!'


main()

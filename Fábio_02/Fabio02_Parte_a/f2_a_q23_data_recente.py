def main():
    dia1 = int(input('Digite a primeira data(dia/mês/ano)\nDia: '))
    mes1 = int(input('Mês: '))
    ano1 = int(input('Ano: '))
    
    dia2 = int(input('Digite a segunda data(dia/mês/ano)\nDia: '))
    mes2 = int(input('Mês: '))
    ano2 = int(input('Ano: '))
    
    dia3 = int(input('Digite a terceira data(dia/mês/ano)\nDia: '))
    mes3 = int(input('Mês: '))
    ano3 = int(input('Ano: '))
    
    data1 = verfificar_data(dia1, mes1, ano1)
    data2 = verfificar_data(dia2, mes2, ano2)
    data3 = verfificar_data(dia3, mes3, ano3)

    if data1 == True and data2 == True and data3 == True:
        data_verificada = comparar_data(dia1, dia2, dia3, mes1, mes2, mes3, ano1, ano2, ano3)
    
        if data_verificada == 4:
            print('As datas digitadas são iguais.')
        else:
            if data_verificada == 1:
                print(f'A data mais recente é {dia1}/{mes1}/{ano1}')
            if data_verificada == 2:
                print(f'A data mais recente é {dia2}/{mes2}/{ano2}')
            if data_verificada == 3:
                print(f'A data mais recente é {dia3}/{mes3}/{ano3}')
    else:
        print('\n>>> DIGITE DATAS VÁLIDAS!!! <<<\n\n')
        main()


def verfificar_data(dia, mes, ano):
    if dia > 0 and mes > 0 and ano > 0:
        if (ano % 4 == 0):
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia <= 31:
                    return True
                else:
                    return False
            elif mes == 2:
                if dia <= 29:
                    return True
                else:
                    return False
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia <= 30:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia <= 31:
                    return True
                else:
                    return False
            elif mes == 2:
                if dia <= 28:
                    return True
                else:
                    return False
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia <= 30:
                    return True
                else:
                    return False
            else:
                return False
    else:
        return False 


def comparar_data(dia1, dia2, dia3, mes1, mes2, mes3, ano1, ano2, ano3):
    data = comparar_ano(ano1, ano2, ano3)
    if data != 4:
        return data
    else:
        data = comparar_mes(mes1, mes2, mes3)
        if data != 4:
            return data
        else:
            data = comparar_dia(dia1, dia2, dia3)
            if data != 4:
                return data
            else:
                return 4


def comparar_ano(ano1, ano2, ano3):
    if (ano1 > ano2 and ano1 > ano3):
        return 1
    if ano2 > ano1 and ano2 > ano3:
        return 2
    if ano3 > ano1  and ano3 > ano2:
        return 3
    if ano1 == ano2 == ano3:
        return 4


def comparar_mes(mes1, mes2, mes3):
    if mes1 > mes2 and mes1 > mes3:
        return 1
    elif mes2 > mes1 and mes2 > mes3:
        return 2
    elif mes3 > mes1 and mes3 > mes2:
        return 3
    else:
        return 4


def comparar_dia(dia1, dia2, dia3):
    if dia1 > dia2 and dia1 > dia3:
        return 1
    elif dia2 > dia1 and dia2 > dia3:
        return 2
    elif dia3 > dia1 and dia3 > dia2:
        return 3
    else:
        return 4


main()

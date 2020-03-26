def main():
    dia = int(input('Digite sua data de nascimento(dia/mês/ano)\nDia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    
    eh_valida = verfificar_data(dia, mes, ano)
    
    print(f'A data que você digitou {eh_valida}.')

def verfificar_data(dia, mes, ano):
    if dia > 0 and mes > 0 and ano > 0:
        
        if (ano % 4 == 0):
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia <= 31:
                    return 'é válida'
                else:
                    return 'não é válida'
            elif mes == 2:
                if dia <= 29:
                    return 'é válida'
                else:
                    return 'não é válida'
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia <= 30:
                    return 'é válida'
                else:
                    return 'não é válida'
            else:
                return 'não é válida'
        else:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                if dia <= 31:
                    return 'é válida'
                else:
                    return 'não é válida'
            elif mes == 2:
                if dia <= 28:
                    return 'é válida'
                else:
                    return 'não é válida'
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia <= 30:
                    return 'é válida'
                else:
                    return 'não é válida'
            else:
                return 'não é válida'
    else:
        return 'não é válida'

main()

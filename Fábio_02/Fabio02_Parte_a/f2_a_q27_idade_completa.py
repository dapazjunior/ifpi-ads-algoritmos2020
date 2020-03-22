def main():
    dia = int(input('Digite sua data de nascimento(dia/mês/ano)\nDia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    
    dia_hoje = int(input('Digite a data de hoje(dia/mês/ano)\nDia: '))
    mes_hoje = int(input('Mês: '))
    ano_hoje = int(input('Ano: '))
    
    nascimento = verfificar_data(dia, mes, ano)
    hoje = verfificar_data(dia_hoje, mes_hoje, ano_hoje)
      
    if nascimento == False and hoje == False:
        print('Datas de nascimento e atual inválidas!')
        main ()
    elif nascimento == False and hoje == True:
        print('Data de nascimento inválida!')
        main()
    elif nascimento == True and hoje == False:
        print('Data atual inválida!')
        main()
    else:
        idade = calcular_idade(dia, mes, ano, dia_hoje, mes_hoje, ano_hoje)
        print(f'Sua idade é {idade}.')


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


def calcular_idade(dia, mes, ano, dia_hoje, mes_hoje, ano_hoje):
    anos = calcular_anos(dia, mes, ano, dia_hoje, mes_hoje, ano_hoje)
    
    meses = calcular_meses(dia, mes, dia_hoje, mes_hoje)
    
    dias = calcular_dias(dia, mes, dia_hoje, mes_hoje, ano)
    
    return f'{anos} ano(s), {meses} mes(es) e {dias} dia(s)'


def calcular_anos(dia, mes, ano, dia_hoje, mes_hoje, ano_hoje):
    anos = ano_hoje - ano - 1
    
    if mes_hoje > mes:
        anos = anos + 1
        return anos
    elif mes_hoje == mes:
        if dia_hoje >= dia:
            anos = anos + 1
            return anos
    
    return anos


def calcular_meses(dia, mes, dia_hoje, mes_hoje):
    meses = 0
    
    if (mes_hoje > mes):
        if dia_hoje > dia:
            meses = mes_hoje - mes
            return meses
        elif dia_hoje < dia:
            meses = 0
            return meses
    
    elif (mes_hoje < mes):
        if dia_hoje > dia:
            meses = (12 - (mes - mes_hoje))
            return meses
        elif dia_hoje < dia:
            meses = (12 - (mes - mes_hoje - 1))
            return meses
    
    return meses


def calcular_dias(dia, mes, dia_hoje, mes_hoje, ano):
    dias = 0
    
    if (dia_hoje < dia):
        dias = dia_menor(dia, mes, dia_hoje, mes_hoje, ano)
        return dias                              
    elif (dia_hoje > dia):
        dias = (dia_hoje - dia)
        return dias
    
    return dias


def dia_menor(dia, mes, dia_hoje, mes_hoje, ano):
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                dias = (31 - dia) + dia_hoje
                return dias
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                dias = (30 - dia) + dia_hoje
                return dias
            else:
                if ano % 4 == 0:
                    dias = (29 - dia) + dia_hoje
                    return dias
                else:
                    dias = (28 - dia) + dia_hoje
                    return dias


main()

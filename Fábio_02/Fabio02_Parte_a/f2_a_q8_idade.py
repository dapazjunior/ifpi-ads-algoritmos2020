def main():
    dia = int(input('Digite sua data de nascimento(dia/mês/ano)\nDia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    
    dia_hoje = int(input('Digite a data de hoje(dia/mês/ano)\nDia: '))
    mes_hoje = int(input('Mês: '))
    ano_hoje = int(input('Ano: '))
    
    idade = calcular_idade(dia, mes, ano, dia_hoje, mes_hoje, ano_hoje)
    
    print(f'Sua idade é {idade} anos.')


def calcular_idade(dia, mes, ano, dia_hoje, mes_hoje, ano_hoje):
    idade = ano_hoje - ano - 1
    
    if mes_hoje > mes:
        idade = idade + 1
        return idade
    elif mes_hoje == mes:
        if dia_hoje >= dia:
            idade = idade + 1
            return idade
    else: idade = idade
    return idade


main()

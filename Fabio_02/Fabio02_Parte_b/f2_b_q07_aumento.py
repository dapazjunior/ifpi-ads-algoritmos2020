def main():
    salario = float(input('Digite seu salário atual: '))
    
    percentual = calcular_percentual(salario) * 100
    aumento = calcular_aumento(salario, percentual)
    novo_salario = calcular_novo_salario(salario, aumento)
    
    print(f'\n>>>>> AUMENTO SALARIAL <<<<<\n\nSalário anterior: R$ {salario:.2f}\nPercentual de aumento: {percentual:.0f} %')
    print(f'Valor do aumento: R$ {aumento:.2f}\nNovo salário: R$ {novo_salario:.2f}\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def calcular_percentual(salario):
    if salario > 0 and salario <= 280:
        return 0.2
    elif salario > 280 and salario <= 700:
        return 0.15
    elif salario > 700 and salario <= 1500:
        return 0.10
    elif salario > 1500:
        return 0.05
    else:
        print('Valor inválido!')
        main()


def calcular_aumento(salario, percentual):
    aumento = salario * percentual / 100
    return aumento

def calcular_novo_salario(salario, aumento):
    novo_salario = salario + aumento
    return novo_salario


main()

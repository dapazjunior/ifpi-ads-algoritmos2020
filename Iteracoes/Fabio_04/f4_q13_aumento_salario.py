def main():
    soma_salario_atual = 0
    soma_novo_salario = 0

    while True:
        salario_atual = float(input('Digite o seu salário atual: '))
        
        if salario_atual == float(0):
            break
        
        aumento_calculado = calcular_aumento(salario_atual)
        novo_salario = salario_atual + aumento_calculado

        print(f'Salário ajustado: R$ {novo_salario:.2f}')

        soma_salario_atual += salario_atual
        soma_novo_salario += novo_salario
        aumento_total = soma_novo_salario - soma_salario_atual
    
    print(f'A soma dos salários atuais é R$ {soma_salario_atual:.2f}')
    print(f'A soma dos salários reajustados é R$ {soma_novo_salario:.2f}')
    print(f'O aumento total é R$ {aumento_total:.2f}')


def calcular_aumento(salario):
    if salario <= 2999.99:
        aumento = salario * 0.25
    elif salario <= 5999.99:
        aumento = salario * 0.20
    elif salario <= 9999.99:
        aumento = salario * 0.15
    else:
        aumento = salario * 0.10
        
    return aumento


main()

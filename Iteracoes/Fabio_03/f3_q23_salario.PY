def main():
    n = int(input('Digite a quantidade de funcionários: '))
    contador = 0

    while contador < n:
        num_id = input('Número de identificação: ')
        horas = int(input(f'Horas trabalhadas: '))
        dependentes = int(input(f'Número de dependentes: '))

        sal_bruto = horas * 12 + dependentes * 40
        inss = sal_bruto * 0.085
        ir = sal_bruto * 0.05

        sal_liquido = sal_bruto - inss - ir

        print('\n>>>>>>>   RECIBO   <<<<<<<\n')
        print(f'Funcionário: {num_id}')
        print(f'Salário bruto: R$ {sal_bruto:.2f}')
        print(f'INSS: - R$ {inss:.2f}')
        print(f'IR: - R$ {ir:.2f}')
        print(f'Salário líquido: R$ {sal_liquido:.2f}\n')
        
        contador += 1

        
main()
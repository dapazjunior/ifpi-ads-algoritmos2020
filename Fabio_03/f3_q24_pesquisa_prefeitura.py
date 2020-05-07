def main():
    n = int(input('Digite a quantidade de habitantes entrevistados: '))
    soma_salario = 0
    soma_filhos = 0

    contador_sal_1000 = 0

    for i in range(1, n + 1):
        print(f'Pessoa {i}:')
        salario = float(input(f'Salário: R$ '))
        filhos = int(input(f'Número de filhos: '))

        soma_salario += salario
        soma_filhos += filhos

        if salario <= 1000:
            contador_sal_1000 += 1
    
    media_salario = soma_salario / n
    media_filhos = soma_filhos / n
    porcentagem_sal_1000 = (contador_sal_1000 / n) * 100

    print(f'Média de salário da população: R$ {media_salario:.2f}')
    print(f'Média de filhos: {media_filhos:.2f}')
    print(f'População com salário até R$ 1000,00: {porcentagem_sal_1000:.1f}%')
        
main()

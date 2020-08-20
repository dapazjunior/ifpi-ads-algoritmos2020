def main():
    alunos = 0
    aprovados = 0
    reprovados = 0

    while True:
        matricula = int(input('Digite a matrícula: '))
        
        if matricula == 0:
            break

        alunos += 1

        nota_1 = int(input('Digite a NOTA 1: '))
        nota_2 = int(input('Digite a NOTA 2: '))
        nota_3 = int(input('Digite a NOTA 3: '))

        media = (2 * nota_1 + 3 * nota_2 + 5 * nota_3) / 10

        if media >= 7:
            aprovados += 1
        else:
            reprovados += 1
    
    print('RESUMO:')
    print(f'{alunos} Alunos\n{aprovados} Aprovados\n{reprovados} Reprovados')


main()

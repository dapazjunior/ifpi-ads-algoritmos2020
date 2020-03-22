def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    
    media = calcular_media(nota1, nota2)
    
    if media >= 7:
        if media != 10:
            print('Aprovado')
        else:
            print('Aprovado com Distinção')
    else:
        print('Aluno REPROVADO.')


def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media


main()
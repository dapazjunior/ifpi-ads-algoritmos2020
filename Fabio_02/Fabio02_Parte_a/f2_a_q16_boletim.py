def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    
    media = calcular_media(nota1, nota2)
    
    if media >= 7:
        print('Aluno APROVADO por média.')
    else:
        nota_ef = float(input('Digite a nota do exame final: '))
        media = calcular_media(media, nota_ef)
        if media >= 5:
            print('Aluno APROVADO no exame final.')
        else:
            print('Aluno REPROVADO.')


def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media


main()

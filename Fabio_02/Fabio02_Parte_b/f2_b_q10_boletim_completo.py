def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    
    media = calcular_media(nota1, nota2)
    conceito = verificar_conceito(media)
    
    resultado = verificar_resultado(conceito)
    
    print(f'\n>>>>> Resultado! <<<<<\n\nNota 1: {nota1}\nNota 2: {nota2}\nMédia: {media}')
    print(f'Conceito: {conceito}\nO aluno foi {resultado}\n\n-=-=-=-=-=-=-=-=-=-=-=\n')


def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media


def verificar_conceito(media):
    if media >= 0 and media <= 4:
        conceito = 'E'
        return conceito
    elif media <= 6:
        conceito = 'D'
        return conceito
    elif media <= 7.5:
        conceito = 'C'
        return conceito
    elif media <= 9:
        conceito = 'B'
        return conceito
    else:
        conceito = 'A'
        return conceito


def verificar_resultado(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        resultado = 'Aprovado'
        return resultado
    else:
        resultado = 'Reprovado'
        return resultado

    
main()

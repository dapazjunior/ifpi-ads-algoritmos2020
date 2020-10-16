from tools_vetor import criar_matriz

def main():
    operacao = input('Digite o código da operação:\nS - Soma\nM - Média\n> ').upper()
    matriz = criar_matriz(12,12)

    if operacao == 'S':
        soma = soma_abaixo_diagonal(matriz)
        print(f'A soma é {soma}')
    
    else:
        media = media_abaixo_diagonal(matriz)
        print(f'A média é {media}')


def soma_abaixo_diagonal(matriz):
    soma = 0
    limite_linha = 12

    for linha in matriz:
        for num in linha[limite_linha:len(matriz)]:
            soma += num
        
        limite_linha -= 1
    
    return soma


def media_abaixo_diagonal(matriz):
    cont = 0
    limite_linha = 12

    for linha in matriz:
        for _ in linha[limite_linha:len(matriz)]:
            cont += 1
        
        limite_linha -= 1

    soma = soma_abaixo_diagonal(matriz)
    media = soma / cont

    return media


main()

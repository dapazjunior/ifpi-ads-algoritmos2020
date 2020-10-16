from tools_vetor import criar_matriz

def main():
    operacao = input('Digite o código da operação:\nS - Soma\nM - Média\n> ').upper()
    matriz = criar_matriz(12,12)

    if operacao == 'S':
        soma = soma_inferior(matriz)
        print(f'A soma é {soma}')
    
    else:
        media = media_inferior(matriz)
        print(f'A média é {media}')


def soma_inferior(matriz):
    soma = 0
    limite_linha = 5
    qtd = 2

    for linha in matriz[7:len(matriz)]:
        for num in linha[limite_linha:(limite_linha + qtd)]:
            print(num)
            soma += num
        
        limite_linha -= 1
        qtd += 2
    
    return soma


def media_inferior(matriz):
    cont = 0
    limite_linha = 5
    qtd = 2

    for linha in matriz[7:len(matriz)]:
        for _ in linha[limite_linha:(limite_linha + qtd)]:
            cont += 1
        
        limite_linha -= 1
        qtd += 2

    soma = soma_inferior(matriz)
    media = soma / cont

    return media


main()

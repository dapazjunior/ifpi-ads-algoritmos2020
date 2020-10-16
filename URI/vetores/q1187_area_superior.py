from tools_vetor import criar_matriz

def main():
    operacao = input('Digite o código da operação:\nS - Soma\nM - Média\n> ').upper()
    matriz = criar_matriz(12,12)

    if operacao == 'S':
        soma = soma_superior(matriz)
        print(f'A soma é {soma}')
    
    else:
        media = media_superior(matriz)
        print(f'A média é {media}')


def soma_superior(matriz):
    soma = 0
    limite_linha = 1
    qtd = 10

    for linha in matriz[0:5]:
        for num in linha[limite_linha:(limite_linha + qtd)]:
            soma += num
        
        limite_linha += 1
        qtd -= 2
    
    return soma


def media_superior(matriz):
    cont = 0
    limite_linha = 1
    qtd = 10

    for linha in matriz[0:5]:
        for _ in linha[limite_linha:(limite_linha + qtd)]:
            cont += 1
        
        limite_linha += 1
        qtd -= 2

    soma = soma_superior(matriz)
    media = soma / cont

    return media


main()

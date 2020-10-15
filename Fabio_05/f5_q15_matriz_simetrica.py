from tools_vetor import criar_matriz

def main():
    ordem = int(input('Qual a ordem da matriz? '))
    
    matriz = criar_matriz(ordem, ordem)

    print(matriz)

    if eh_simetrica(matriz):
        print('A matriz é simétrica!')
    else:
        print('A matriz não é simétrica!')


def eh_simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    
    return True


main()
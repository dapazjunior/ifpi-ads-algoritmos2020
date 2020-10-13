from tools_vetor import criar_matriz, somar_diag_pri, somar_diag_sec

def main():
    ordem = int(input('Qual a ordem da matriz quadrada? '))
    matriz = criar_matriz(ordem, ordem)
    print('Matriz:')
    print(matriz)

    diag_pri = somar_diag_pri(matriz)
    print(f'Soma da diagonal principal: {diag_pri}')

    diag_sec = somar_diag_sec(matriz)
    print(f'Soma da diagonal secundária: {diag_sec}')


main()
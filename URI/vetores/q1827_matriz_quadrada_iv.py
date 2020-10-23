def main():
    while True:
        ordem = int(input('Ordem da matriz quadrada: '))
        
        if ordem == 0:
            break

        matriz = []
        adicionar_matriz(matriz, ordem)

        for linha in matriz:
            print(linha)


def adicionar_matriz(matriz, ordem):
    pass


main()

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
    for num in range(ordem):
        linha = criar_linha(num, ordem)
        matriz.append(linha)


def criar_linha(num, ordem):
    linha = []
    for _ in range(ordem):
        linha.append(2**num)
        num += 1
    
    return linha


main()

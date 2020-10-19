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
    for num in range(0, ordem):
        linha = adicionar_linha(num + 1)
        matriz.append(linha)
        numero = len(matriz)
        
        for linha in matriz:
            if numero > 1:
                linha.append(numero)
                numero -= 1


def adicionar_linha(numero):
    linha = []

    for i in range(numero, 0, -1):
        linha.append(i)
    
    return linha


main()

def main():
    while True:
        ordem = int(input('Ordem da matriz quadrada: '))
        
        if ordem == 0:
            break

        matriz = criar_matriz(ordem)
        calcular(matriz)

        for i in range(ordem):
            print(matriz[i])


def criar_matriz(ordem):
    matriz = []
    
    for i in range(0, ordem):
        matriz.append([])

        for _ in range(0, ordem):
            matriz[i].append(0)
    
    return matriz


def calcular(matriz):
    ordem = len(matriz)

    if ordem % 2 == 0:
        limite = ordem // 2
    else:
        limite = ordem // 2 + 1
    
    minimo = 0
    maximo = ordem
    numero = 0

    for _ in range(0, limite):
        numero += 1

        for i in range(minimo, maximo):
            for j in range(minimo, maximo):
                matriz[i][j] = numero

        minimo += 1
        maximo -= 1


def eh_par(num):
    if num % 2 == 0:
        return True
    
    else:
        return False


main()
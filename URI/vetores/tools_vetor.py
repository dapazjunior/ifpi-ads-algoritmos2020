def criar_vetor(n):
    vetor = []
    
    for i in range(n):
        elemento = input(f'Posição [{i}]: ')
        vetor.append(elemento)
    
    return vetor


def criar_vetor_num(n):
    vetor = []
    
    for i in range(n):
        elemento = int(input(f'Posição [{i}]: '))
        vetor.append(elemento)
    
    return vetor


def criar_matriz(linhas, colunas):
    matriz = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = float(input(f'Elemento "{i},{j}": '))
            linha.append(valor)
        
        matriz.append(linha)

    return matriz


def somar_diag_pri(matriz):
    if eh_quadrada(matriz):
        ordem = len(matriz)

        soma = 0
        for i in range(ordem):
            soma += matriz[i][i]
    
    else:
        print('Matriz não é quadrada!')
        return EOFError
    
    return soma


def somar_diag_sec(matriz):
    if eh_quadrada(matriz):
        ordem = len(matriz)

        soma = 0
        for i in range(ordem):
            soma += matriz[i][ordem - i - 1]
    
    else:
        print('Matriz não é quadrada!')
        return EOFError
    
    return soma


def eh_quadrada(matriz):
    verifica = True
    
    for i in range(len(matriz)):
        if len(matriz) != len(matriz[i]):
            verifica = False
    
    return verifica


def somar_linha_matriz(matriz, num_linha):
    soma = 0
    
    for num in matriz[num_linha]:
        soma += num
    
    return soma


def somar_coluna_matriz(matriz, num_coluna):
    soma = 0
    
    for linha in matriz:
        soma += linha[num_coluna]
    
    return soma
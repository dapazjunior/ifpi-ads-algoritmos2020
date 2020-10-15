from tools_vetor import somar_linha_matriz, criar_matriz
from math import inf

def main():
    ordem = int(input('Qual a ordem da matriz? '))
    
    matriz = criar_matriz(ordem, ordem)

    maior_linha = 0
    soma_maior = -inf

    menor_linha = 0
    soma_menor = +inf

    for linha in range(len(matriz)):
        soma_linha = somar_linha_matriz(matriz, linha)

        if soma_linha > soma_maior:
            maior_linha = linha
            soma_maior = soma_linha
        
        if soma_linha < soma_menor:
            menor_linha = linha
            soma_menor = soma_linha
    

    print(f'A maior soma é {soma_maior} referente à linha "{maior_linha}"')
    print(f'A menor soma é {soma_menor} referente à linha "{menor_linha}"')


main()

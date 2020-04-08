def main():
    maior = -1
    posicao = -1
    for i in range (100):
        numero = int(input())
        if numero > maior:
            maior = numero
            posicao = i + 1
    
    print(maior)
    print(posicao)


main()

def main():

    n = int(input("Número: "))
    resultado(n)


def resultado(n):
    perfeito = 0 # contador
    while n > 0:
        quadrado = n ** 0.5 # tirar raiz quadrada
        if quadrado % 1 == 0: # verifica o resto da divisão
            print(f'{n} - {quadrado}')
            perfeito += 1 # incrementa o contador
            if perfeito == 1: # para a função se achar o primeiro resultado
                break
        n -= 1


main()
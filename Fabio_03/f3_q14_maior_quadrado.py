def main():
    n = int(input('Digite um número: '))
    maior_quadrado = 0

    for i in range(1, n + 1):
        quadrado = i ** 2

        if quadrado <= n:
            maior_quadrado = quadrado
    
    print(maior_quadrado)


main()

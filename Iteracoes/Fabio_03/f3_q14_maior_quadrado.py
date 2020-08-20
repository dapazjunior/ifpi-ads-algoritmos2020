def main():
    n = int(input('Digite um número: '))
    num = 0

    while (num ** 2) <= n:
        maior_quadrado = num ** 2
        num += 1
    
    print(f'Maior quadrado: ', maior_quadrado)


main()
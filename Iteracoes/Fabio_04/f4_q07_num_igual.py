def main():
    n = int(input('Digite um número: '))

    cont_n = 0

    while cont_n == 0:
        c = int(input('Digite um número: '))

        if c == n:
            cont_n += 1
            print('Valor encontrado!')


main()

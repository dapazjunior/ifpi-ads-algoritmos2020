def main():
    x = int(input('Digite o valor de X: '))
    n = int(input('Digite o valor de N: '))

    while n != 2:
        div = x / n
        print(f'A divisão de {x} por {n} é {div}')

        x = div
        n -= 1


main()

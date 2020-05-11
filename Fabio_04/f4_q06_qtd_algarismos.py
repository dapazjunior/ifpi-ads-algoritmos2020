def main():
    n = int(input('Digite um número: '))
    cont_n = 0

    while n >= 1:
        n = n / 10
        cont_n += 1

    print(f'O número digitado tem {cont_n} algarismos.')


main()

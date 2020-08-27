def main():
    n = int(input('Digite um número: '))

    soma = 0

    for i in range(1, n + 1):
        termo = (2*i - 1)/ i
        soma += termo
    
    print(soma)


main()

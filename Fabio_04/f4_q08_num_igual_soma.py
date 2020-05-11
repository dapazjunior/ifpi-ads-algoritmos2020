def main():
    x = int(input('Digite o valor de X: '))
    lista = []
    n = -1

    while n < 1:
        num = int(input('Digite um número: '))
        lista.append(num)
        n += 1

    if (lista[0] + lista[1] != x):
        while (lista[n] + lista[n - 1]) != x:
            num = int(input('Digite um número: '))
            lista.append(num)
            n += 1
    
    print(lista)
    print(f'A soma de {lista[n -1]} e {lista[n]} é igual a X.')


main()

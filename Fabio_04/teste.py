def main():
    numero_1 = int(input('Numero 1: '))
    numero_2 = int(input('Numero 2: '))
    
    multiplicacao = valor_multiplicacao(numero_1,numero_2)

    print('Valor da multiplicacao eh: %d'%multiplicacao)


def valor_multiplicacao(n1,n2):
    multiplicacao = n1
    contador = 1
    
    while contador < n2:
        multiplicacao = multiplicacao + n1
        contador += 1

    return multiplicacao

if __name__ == '__main__':
    main()
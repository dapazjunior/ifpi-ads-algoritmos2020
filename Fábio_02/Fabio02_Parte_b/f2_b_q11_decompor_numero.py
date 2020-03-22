def main():
    numero = int(input('Digite um numero inteiro menor que 1000: '))
    
    centena = calc_centena(numero)
    dezena = calc_dezena(numero)
    unidade = calc_unidade(numero)
    
    print_centena(centena, dezena, unidade)
    print_dezena(centena, dezena, unidade)
    print_unidade(centena, dezena, unidade)


def calc_centena(numero):
    centena = numero // 100
    return centena


def calc_dezena(numero):
    dezena = (numero % 100) // 10
    return dezena


def calc_unidade(numero):
    unidade = (numero % 100) % 10
    return unidade


def print_centena(centena, dezena, unidade):
    if centena == 1:
        print(f'{centena} centena', end = '')
    elif centena != 0:
        print(f'{centena} centenas', end = '')
    else:
        pass


def print_dezena(centena, dezena, unidade):
    if centena == 0:
        if unidade == 0:
            if dezena == 1:
                print(f'{dezena} dezena')
            elif dezena != 0:
                print(f'{dezena} dezenas')
            else:
                pass
        elif unidade != 0:
            if dezena == 1:
                print(f'{dezena} dezena', end = '')
            elif dezena != 0:
                print(f'{dezena} dezenas', end = '')
            else:
                pass
    else:
        if unidade == 0:
            if dezena == 1:
                print(f' e {dezena} dezena')
            elif dezena != 0:
                print(f' e {dezena} dezenas')
            else:
                pass
        elif unidade != 0:
            if dezena == 1:
                print(f', {dezena} dezena', end = '')
            elif dezena != 0:
                print(f', {dezena} dezenas', end = '')
            else:
                pass


def print_unidade(centena, dezena, unidade):
    if centena == 0 and dezena == 0:
        if unidade == 1:
            print(f'{unidade} unidade')
        elif unidade != 0:
            print(f'{unidade} unidades')
        else:
            pass
    else:
        if unidade == 1:
            print(f' e {unidade} unidade')
        elif unidade != 0:
            print(f' e {unidade} unidades')
        else:
            pass


main()

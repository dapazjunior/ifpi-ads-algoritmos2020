def main():
    numero = int(input('Número inteiro(até 3 algarismos): '))
    
    centena = alg_centena_romano(numero)
    dezena = alg_dezena_romano(numero)
    unidade = alg_unidade_romano(numero)
    
    romano = centena + dezena + unidade
    
    print(f'O número {numero} em algarismos romanos é "{romano}".')
    
def alg_centena_romano(num):
    cent = num // 100
    
    if cent == 0:
        return ''
    if cent > 0 and cent < 4:
        return 'C' * cent
    elif cent == 4:
        return 'CM'
    elif cent > 4 and cent < 9:
        return 'D' + 'C' * (cent - 5)
    else:
        return 'CM'


def alg_dezena_romano(num):
    dez = (num % 100) // 10
    
    if dez == 0:
        return ''
    if dez > 0 and dez < 4:
        return 'X' * dez
    elif dez == 4:
        return 'XL'
    elif dez > 4 and dez < 9:
        return 'L' + 'X' * (dez - 5)
    else:
        return 'XC'


def alg_unidade_romano(num):
    und = (num % 100) % 10
    
    if und == 0:
        return ''
    if und > 0 and und < 4:
        return 'I' * und
    elif und == 4:
        return 'IV'
    elif und > 4 and und < 9:
        return 'V' + 'I' * (und - 5)
    else:
        return 'IX'


main()

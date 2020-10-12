from tools_vetor import criar_vetor

def main():
    print('Digite os algarismos de um número binario (8 algarismos):')
    binario = criar_vetor(8)

    decimal = converter_decimal(binario)
    hexadec = converter_hexadec(binario)

    num_bin = escrever_bin(binario)
    
    print(f'Número Binário: {num_bin}')
    print(f'Número Decimal: {decimal}')
    print(f'Número Hexadecimal: {hexadec}')


def escrever_bin(binario):
    num_bin = ''
    for num in binario:
        num_bin += num
    
    return num_bin


def converter_decimal(vetor_bin):
    cont = len(vetor_bin) - 1
    dec = 0
    for i in vetor_bin:
        dec += int(i) * (2**cont)
        cont -= 1
    
    return dec


def converter_hexadec(vetor_bin):
    alg1 = converter_decimal(vetor_bin[0:4])
    alg2 = converter_decimal(vetor_bin[4:8])
    print(alg1)
    print(alg2)

    alg1 = verificar_hexdec(alg1)
    alg2 = verificar_hexdec(alg2)

    hexadec = alg1 + alg2
    return hexadec


def verificar_hexdec(dig):
    if dig >= 0 and dig <= 9:
        dig = str(dig)
    else:
        if dig == 10:
            dig = 'A'
        if dig == 11:
            dig = 'B'
        if dig == 12:
            dig = 'C'
        if dig == 13:
            dig = 'D'
        if dig == 14:
            dig = 'E'
        if dig == 15:
            dig = 'F'
    
    return dig


main()
def main():
    num = int(input('Digite um número inteiro na base decimal: '))
    num_dig = num
    num_hex = ''
    num_bin = 0
    divisoes_bin = 0
    
    while num != 0:
        digito = num % 2
        num_bin = num_bin + digito * (10 ** divisoes_bin)
        num = num // 2
        divisoes_bin += 1
    
    print(f'Binário: {num_bin}')

    while num_dig != 0:
        digito = num_dig % 16
        digito = verificar_decimal(digito)
        num_hex = digito + num_hex
        
        num_dig = num_dig // 16
    
    print(f'Hexadecimal: {num_hex}')

def verificar_decimal(dig):
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

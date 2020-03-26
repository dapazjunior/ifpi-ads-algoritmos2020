def main():
    num = float(input('Digite um número: '))
    
    pos_ou_neg = verificar_pos_ou_neg(num)
    
    print(f'O número {num} é {pos_ou_neg}.')


def verificar_pos_ou_neg(num):
    if num > 0:
        return 'positivo'
    elif num < 0:
        return 'negativo'
    else:
        return 'neutro'


main()

def main():
    num = float(input('Digite um número: '))
    
    verificar_se_inteiro(num)


def verificar_se_inteiro(num):
    if int(num) == num:
        print('O número é inteiro.')
    else:
        print('O número é decimal.')


main()

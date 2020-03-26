def main():
    num = int(input('Digite um número inteiro: '))
    
    verificar_se_par(num)
    
    
def verificar_se_par(num):
    if (num % 2 == 0):
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')


main()

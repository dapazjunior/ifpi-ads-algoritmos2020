from random import randint

def main():
    aleatorio = randint(0, 1000)
    cont_num = 0
    numero = -1
    
    while numero != aleatorio:
        numero = int(input('Digite um número: '))
        cont_num += 1
        
        if numero == aleatorio:
            print('ACERTOU')
        elif numero < aleatorio:
            print('TENTE UM NÚMERO MAIOR!')
        else:
            print('TENTE UM NÚMERO MENOR!')
    
    print(f'Você fez {cont_num} tentativas')


main()

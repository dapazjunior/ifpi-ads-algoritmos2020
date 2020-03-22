def main():
    num = int(input('Digite um número inteiro entre 0 e 100: '))
        
    primo = eh_primo(num)
    
    if num > 0 and num <= 100:
        print(f'O número digitado {primo} primo.')
    
    else:
        print(f'O número {num} não está entre 0 e 100.')
        main()


def eh_primo(num):
    if num == 0 or num == 1:
        return 'não é'
    elif num == 2:
        return 'é'
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        return 'é'
    else:
        return 'não é'

main()

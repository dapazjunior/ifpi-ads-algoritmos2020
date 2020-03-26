def main():
    num = int(input('Digite um número inteiro entre 0 e 100: '))
        
    primo = eh_primo(num)
    
    print(f'O número digitado {primo} primo.')


def eh_primo(num):
    multiplos = 0
    
    for valores in range(1, num + 1):
        if (num % valores == 0):
            multiplos = multiplos + 1
    
    if multiplos == 2:
        return 'é'
    else:
        return 'não é'

main()

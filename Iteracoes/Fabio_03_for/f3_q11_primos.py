def main():
    lim_inf = int(input('Digite o Limite Inferior: '))
    lim_sup = int(input('Digite o Limite Superior: '))

    for i in range(lim_inf, lim_sup):
        if eh_primo(i):
            print (i)


def eh_primo(num):
    multiplos = 0
    
    for c in range(1, num + 1):
        if (num % c == 0):
            multiplos +=  1
    
    if multiplos == 2:
        return True
    else:
        return False


main()

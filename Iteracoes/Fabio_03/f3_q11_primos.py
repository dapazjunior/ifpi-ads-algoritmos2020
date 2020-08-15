def main():
    lim_inf = int(input('Digite o Limite Inferior: '))
    lim_sup = int(input('Digite o Limite Superior: '))

    while lim_inf <= lim_sup:
        if eh_primo(lim_inf):
            print (lim_inf)
        
        lim_inf += 1


def eh_primo(num):
    divisores = 0
    divisor = 1
    
    while divisor <= num:
        if (num % divisor == 0):
            divisores +=  1
        
        divisor += 1
    
    if divisores == 2:
        return True
    else:
        return False


main()

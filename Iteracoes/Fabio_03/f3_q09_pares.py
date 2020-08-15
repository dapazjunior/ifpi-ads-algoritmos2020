def main():
    lim_inf = int(input('Digite o Limite Inferior: '))
    lim_sup = int(input('Digite o Limite Superior: '))

    while lim_inf <= lim_sup:
        if (lim_inf % 2) == 0:
            print (lim_inf)
        
        lim_inf += 1

main()

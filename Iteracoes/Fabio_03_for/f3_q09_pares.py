def main():
    lim_inf = int(input('Digite o Limite Inferior: '))
    lim_sup = int(input('Digite o Limite Superior: '))

    for i in range(lim_inf, lim_sup + 1):
        if (i % 2) == 0:
            print (i)

main()

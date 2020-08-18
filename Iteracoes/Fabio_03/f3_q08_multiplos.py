def main():
    n = int(input('Digite um número: '))
    lim_inf = int(input('Digite o Limite Inferior: '))
    lim_sup = int(input('Digite o Limite Superior: '))
    cont_multiplos = 0
    
    possivel_mult = lim_inf

    while possivel_mult <= lim_sup:
        if (possivel_mult % n) == 0:
            cont_multiplos = cont_multiplos + 1
            print(possivel_mult)
        
        possivel_mult += 1
    
    print(f'O número {n} tem {cont_multiplos} múltiplos entre {lim_inf} e {lim_sup}')

main()

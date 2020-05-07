def main():
    n = int(input('Digite um número: '))
    lim_inf = int(input('Digite o Limite Inferior: '))
    lim_sup = int(input('Digite o Limite Superior: '))
    cont_multiplos = 0

    for i in range(lim_inf, lim_sup + 1):
        if (i % n) == 0:
            cont_multiplos = cont_multiplos + 1
    
    print(f'O número {n} tem {cont_multiplos} múltiplos entre {lim_inf} e {lim_sup}')

main()

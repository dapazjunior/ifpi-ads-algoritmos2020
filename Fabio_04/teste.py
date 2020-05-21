def main():
    nome,altura,peso = ficha()
    
    nome_alt,alt,nome_baix,baix,nome_magr,magr,nome_gord,gord = concurso(altura,peso,nome)
    
    print('A modelo mais alta é: %s'%nome_alt,'. Altura: %.1f'%alt)
    print('A modelo mais baixa é: %s'%nome_baix,'. Altura: %.1f'%baix)
    print('A modelo mais magra é: %s'%nome_magr,'. Peso: %.1f'%magr)
    print('A modelo mais gorda é: %s'%nome_gord,'. Peso: %.1f'%gord)


def ficha():
    nome = input('Digite o nome: ')
    
    if nome != 'FIM':
        altura = float(input('Digite a altura: '))
        peso = float(input('Digite o peso: '))
    else:
        altura = 0
        peso = 0
        
    return nome,altura,peso,


def concurso(altura,peso,nome):
    baixa = altura
    alta = altura
    magra = peso
    gorda = peso
    
    while nome != 'FIM':
        if peso <= magra:
            magra = peso
            nome_magra = nome
        elif peso >= gorda:
            gorda = peso
            nome_gorda = nome
        
        if altura <= baixa:
            baixa = altura
            nome_baixa = nome
        elif altura >= alta:
            alta = altura
            nome_alta = nome
        nome,altura,peso = ficha()
    
    return nome_alta,alta,nome_baixa,baixa,nome_magra,magra,nome_gorda,gorda


if __name__ == '__main__':
    main()
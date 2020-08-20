from math import inf
def main():
    altura_mais_alta = 0
    altura_mais_baixa = inf
    peso_mais_gorda = 0
    peso_mais_magra = inf
    
    while True:
        nome = input('Nome da candidata: ').upper()
        
        if nome == 'FIM':
            break
        
        altura = float(input('Altura da candidata: '))
        peso = float(input('Peso da candidata: '))
        print('')
        
        if altura >= altura_mais_alta:
            nome_mais_alta = nome
            altura_mais_alta = altura
        
        if altura < altura_mais_baixa:
            nome_mais_baixa = nome
            altura_mais_baixa = altura
        
        if peso > peso_mais_gorda:
            nome_mais_gorda = nome
            peso_mais_gorda = peso
        
        if peso < peso_mais_magra:
            nome_mais_magra = nome
            peso_mais_magra = peso

    
    print(f'\nMais alta: {nome_mais_alta} - Altura: {altura_mais_alta:.2f} m')
    print(f'Mais baixa: {nome_mais_baixa} - Altura: {altura_mais_baixa:.2f} m')
    print(f'Mais magra: {nome_mais_magra} - Peso: {peso_mais_magra:.2f} kg')
    print(f'Mais gorda: {nome_mais_gorda} - Peso: {peso_mais_gorda:.2f} kg')


main()

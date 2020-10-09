def main():
    verbo = input('Digite um verbo regular de segunda conjugação:\n> ')
    conjugar(verbo)


def conjugar(verbo):
    verbo = verbo.lower()
    index_fim = len(verbo) - 2
    
    if verbo[index_fim:index_fim + 2] == 'er':
        print(f'Verbo: "{verbo}"')
        radical = verbo[0:index_fim]
        print(f'Radical: "{radical}"\n')

        print('CONJUGAÇÃO\nPresente do Indicativo:\n' + \
          f'Eu {radical}o\n' + \
          f'Tu {radical}es\n' + \
          f'Ele {radical}e\n' + \
          f'Nós {radical}emos\n' + \
          f'Vós {radical}eis\n' + \
          f'Eles {radical}em\n' )
    
    else:
        print('Verbo inválido! Tente novamente!')
        main()


main()

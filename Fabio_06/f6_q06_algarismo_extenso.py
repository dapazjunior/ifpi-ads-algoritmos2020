def main():
    frase = input('Digite uma frase:\n> ')
    
    nova_frase = num_extenso(frase)
    
    print(f'Escrevendo algarismos por extenso:\n> {nova_frase}')


def num_extenso(string):
    nova_string = ''
    
    for i in string:
        if i == '1':
            nova_string += 'um'
        elif i == '2':
            nova_string += 'dois'
        elif i == '3':
            nova_string += 'três'
        elif i == '4':
            nova_string += 'quatro'
        elif i == '5':
            nova_string += 'cinco'
        elif i == '6':
            nova_string += 'seis'
        elif i == '7':
            nova_string += 'sete'
        elif i == '8':
            nova_string += 'oito'
        elif i == '9':
            nova_string += 'nove'
        elif i == '0':
            nova_string += 'zero'
        else:
            nova_string += i
    
    return nova_string


main()
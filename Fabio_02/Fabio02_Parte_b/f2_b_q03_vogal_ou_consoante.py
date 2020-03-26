def main():
    letra = input('Digite uma letra: ')
    letra = letra.lower()
    
    v_ou_c = verificar_se_v_ou_c(letra)
    
    print(f'{v_ou_c}')


def verificar_se_v_ou_c(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return f'A letra "{letra}" é vogal.'
    else:
        return f'A letra "{letra}" é consoante.'


main()

def main():
    letra = str(input('Digite uma letra: '))
    
    m_ou_f = verificar_se_m_ou_f(letra)
    
    print(f'{m_ou_f}')


def verificar_se_m_ou_f(letra):
    if letra == 'M' or letra == 'm':
        return 'Masculino'
    elif letra == 'F' or letra == 'f':
        return 'Feminino'
    else:
        return 'Sexo Inválido!'


main()

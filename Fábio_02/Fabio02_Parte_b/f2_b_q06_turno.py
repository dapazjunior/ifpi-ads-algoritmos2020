def main():
    turno = input('Qual o turno que você estuda?\nM - Matutino\nV - Vespertino\nN - Noturno\n>>> ').upper()
    
    saudacao = verificar_turno(turno)
    
    print (saudacao)


def verificar_turno(turno):
    if turno == 'M':
        return 'Bom Dia!'
    elif turno == 'V':
        return 'Boa Tarde!'
    elif turno == 'N':
        return 'Boa Noite!'
    else:
        return 'Valor Inválido!'


main()

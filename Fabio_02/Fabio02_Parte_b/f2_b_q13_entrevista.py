def main():
    print('Responda as perguntas com S(sim) e N(Não).')
    a = input('Telefonou para a vítima?\n>>> ').lower()
    b = input('Esteve no local do crime?\n>>> ').lower()
    c = input('Mora perto da vítima?\n>>> ').lower()
    d = input('Devia para a vítima?\n>>> ').lower()
    e = input('Já trabalhou com a vítima?\n>>> ').lower()
    
    sim = verificar_se_suspeito(a, b, c, d, e)
    
    if sim == 2:
        print('\nVocê é Suspeito\n')
    elif sim == 3 or sim == 4:
        print('\nVocê é Cúmplice\n')
    elif sim == 5:
        print('\nVocê é Assassino\n')
    else:
        print('\nVocê é Inocente\n')


def verificar_se_suspeito(a, b, c, d, e):
    sim = 0
    
    if a == 's':
        sim = sim + 1
    if b == 's':
        sim = sim + 1
    if c == 's':
        sim = sim + 1
    if d == 's':
        sim = sim + 1
    if e == 's':
        sim = sim + 1
    
    return sim


main()

def main():
    palavras = ler_palavras()
    
    menu = '> > > > WordPlay < < < <\n' \
        + '1 - Palavras com mais de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Evitar letras proibidas\n' \
        + '4 - Use apenas as letras escolhidas\n' \
        + '5 - Use todas as letras\n' \
        + '6 - É ordem alfabética?\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))
    
    while opcao != 0:
        if opcao == 1:
            palavras_mais_de_20_letras(palavras)
        
        elif opcao == 2:
            palavras_sem_e(palavras)
        
        elif opcao == 3:
            evitar_letras_proibidas(palavras)
        
        elif opcao == 4:
            usar_letras_escolhidas(palavras)
        
        elif opcao == 5:
            usar_todas_letras(palavras)
        
        elif opcao == 6:
            em_ordem_alfabetica(palavras)
            
        else:
            print('Opção inválida! Tente novamente...')
        
        input('\nPressione ENTER para continuar...')
        opcao = int(input(menu))


def palavras_mais_de_20_letras(palavras):
    print('\n> PALAVRAS COM MAIS DE 2 LETRAS:\n')
    
    for palavra in palavras:
        if len(palavra) > 20:
            print(palavra)


def palavras_sem_e(palavras):
    print('\n> PALAVRAS SEM A LETRA "E":\n')
    
    palavras_total = len(palavras)
    palavras_sem_e = 0
    
    for palavra in palavras:
        if tem_letra_e(palavra):
            pass
        else:
            print(palavra)
            palavras_sem_e += 1
    
    percentual_sem_e = palavras_sem_e / palavras_total * 100
    
    print(f'\n{percentual_sem_e:.1f} % das palvra que não tem a letra "e"')


def tem_letra_e(palavra):
    verificacao = False
    
    for letra in palavra:
        if letra == 'e':
            verificacao = True
    
    return verificacao


def evitar_letras_proibidas(palavras):
    print('\n> LETRAS PROIBIDAS\n')
    
    letras = input('Digite as letras que não serão utilizadas: ')
    for palavra in palavras:
        if nao_tem_letras(palavra, letras):
            print(palavra)


def nao_tem_letras(palavra, letras):
    verificacao = True
    
    for c in palavra:
        for i in letras:
            if c == i:
                verificacao = False
    
    return verificacao                


def usar_letras_escolhidas(palavras):
    print('\n> USAR SOMENTE AS LETRAS ESCLHIDAS\n')
    
    letras = input('Digite as letras escolhidas: ')
    
    for palavra in palavras:
        if so_tem_letras(letras, palavra):
            print(palavra)


def so_tem_letras(letras, palavra):
    indice_letra = 0
    verificacao = True
    
    while indice_letra < len(letras):
        for c in palavra:
            if c not in letras:
                verificacao = False
        
        indice_letra += 1
    
    return verificacao


def usar_todas_letras(palavras):
    print('\n> PALAVRAS QUE USAM TODAS AS LETRAS\n')
    
    letras = input('Digite as letras desejadas: ')
    cont_palavras = 0
    
    for palavra in palavras:
        if tem_todas_letras(letras, palavra):
            print(palavra)
            
            cont_palavras += 1
    
    print(f'Existem {cont_palavras} palavras com as letras "{letras}".')


def tem_todas_letras(letras, palavra):
    indice_letra = 0
    verificacao = True
    
    while indice_letra < len(letras):
        for c in letras:
            if c not in palavra:
                verificacao = False
        
        indice_letra += 1
    
    return verificacao


def em_ordem_alfabetica(palavras):
    print('\n>PALAVRAS EM ORDEM ALAFABÉTICA\n')
    
    for palavra in palavras:
        if esta_em_ordem(palavra):
            print(palavra)


def esta_em_ordem(palavra):
    indice = 0
    
    while indice < (len(palavra) - 1):
        if ord(palavra[indice]) > ord(palavra[indice + 1]):
            return False
        
        indice += 1
    
    return True


def ler_palavras():
    arquivo = open('words.txt')
    palavras = []
    
    for linha in arquivo:
        palavra = linha.strip()
        palavras.append(palavra)
    
    return palavras


main()
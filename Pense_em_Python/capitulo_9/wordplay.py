def main():
    palavras = ler_palavras()
    
    menu = '> > > > WordPplay < < < <\n' \
        + '1 - Palavras com mais de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Evitar letras proibidas\n' \
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
            
        else:
            print('Opção inválida! Tente novamente...')
        
        input('\nPressione ENTER para continuar...')
        opcao = int(input(menu))


def palavras_mais_de_20_letras(palavras):
    print('> PALAVRAS COM MAIS DE 2 LETRAS:\n')
    
    for palavra in palavras:
        if len(palavra) > 20:
            print(palavra)


def palavras_sem_e(palavras):
    print('> PALAVRAS SEM A LETRA "E":\n')
    
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
    print('> LETRAS PROIBIDAS\n')
    
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


def ler_palavras():
    arquivo = open('words.txt')
    palavras = []
    
    for linha in arquivo:
        palavra = linha.strip()
        palavras.append(palavra)
    
    return palavras


main()
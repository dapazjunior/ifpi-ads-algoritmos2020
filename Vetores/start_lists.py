def main():
    lista = []
    
    menu_principal(lista)
    

def menu_principal(lista):
    menu = '> > > ListsPlay < < <\n'
    menu += '1 - INSERIR VALORES\n'
    menu += '2 - MOSTRAR VALORES\n'
    menu += '3 - REMOVER VALORES\n'
    menu += '4 - CONTADORES\n'
    menu += '5 - MÉDIA DOS VALORES\n'
    menu += '6 - OPERAÇÕES COM OS VALORES\n'
    menu += '0 - SAIR\n'
    menu += '\nOpção >>> '
    
    opcao = int(input(menu))
        
    if opcao == 1:
        inserir(lista)
    elif opcao == 2:
        mostrar(lista)
    elif opcao == 3:
        remover(lista)
    elif opcao == 4:
        contar(lista)
    elif opcao == 5:
        media(lista)
    elif opcao == 0:
        print('Fim do programa!')
    else:
        print('Opção Inválida!\n')
        
        input('Aperte ENTER para continuar... \n')
        menu_principal(lista)


def inserir(lista):
    menu_inserir = '\n> > > INSERIR < < <\n'
    menu_inserir += '1 - Valor no ínicio\n'
    menu_inserir += '2 - Valor no final\n'
    menu_inserir += '3 - Valor em posição específica\n'
    menu_inserir += '\nOpção >>> '
    
    opcao_inserir = int(input(menu_inserir))
    
    if opcao_inserir == 1:
        lista = inserir_inicio(lista)
    elif opcao_inserir == 2:
        lista = inserir_final(lista)
    elif opcao_inserir == 3:
        lista = inserir_posicao(lista)
    else:
        print('\nOpção Inválida!')
        
    if continuar():
        inserir(lista)
    else:
        input('Aperte ENTER para continuar... \n')
        menu_principal(lista)


def inserir_inicio(lista):
    qtd = int(input('\nQuantos elementos deseja inserir?\n> '))
    lista_add = []
    
    for i in range(qtd):
        valor = input(f'Elemento "{i}": ')
        lista_add.append(valor)
    
    lista = lista_add + lista
    return lista


def inserir_final(lista):
    qtd = int(input('\nQuantos elementos deseja inserir?\n> '))
    pos = len(lista)
    
    for i in range(qtd):
        valor = input(f'Elemento "{pos + i}": ')
        lista.append(valor)
    
    return lista


def inserir_posicao(lista):
    qtd = int(input('\nQuantos elementos deseja inserir?\n> '))
    
    for _ in range(qtd):
        pos = int(input('\nPosição a ser inserido: '))
        valor = int(input(f'Elemento "{pos}": '))
        lista.insert(pos, valor)
    
    return lista


def mostrar(lista):
    menu_mostar = '\n> > > MOSTRAR < < <\n'
    menu_mostar += '1 - Todos os valores\n'
    menu_mostar += '2 - Valores em posição específica\n'
    menu_mostar += '\nOpção >>> '
    
    opcao_mostrar = int(input(menu_mostar))
    
    if opcao_mostrar == 1:
        mostrar_todos(lista)
    elif opcao_mostrar == 2:
        mostrar_posicao(lista)
    else:
        print('\nOpção Inválida!')
        
    if continuar():
        mostrar(lista)
    else:
        input('Aperte ENTER para continuar... \n')
        menu_principal(lista)


def mostrar_todos(lista):
    print(lista)


def mostrar_posicao(lista):
    pos = int(input('Digite a posição: '))
    print(f'Elemento "{pos}": {lista[pos]}')


def remover(lista):
    menu_remover = '\n> > > REMOVER < < <\n'
    menu_remover += '1 - No ínicio\n'
    menu_remover += '2 - No final\n'
    menu_remover += '3 - Valores em posição específica\n'
    menu_remover += '4 - Todos os valores\n'
    menu_remover += '\nOpção >>> '
    
    opcao_remover = int(input(menu_remover))
    
    if opcao_remover == 1:
        lista = remover_inicio(lista)
    elif opcao_remover == 2:
        lista = remover_final(lista)
    elif opcao_remover == 3:
        lista = remover_posicao(lista)
    elif opcao_remover == 4:
        remover_todos(lista)
    else:
        print('\nOpção Inválida!')
        
    if continuar():
        remover(lista)
    else:
        input('Aperte ENTER para continuar... \n')
        menu_principal(lista)


def remover_inicio(lista):
    qtd = int(input('\nQuantos elementos remover?\n> '))
    
    for _ in range(qtd):
        lista.pop(0)
    
    return lista


def remover_final(lista):
    qtd = int(input('\nQuantos elementos remover?\n> '))
    
    for _ in range(qtd):
        lista.pop(len(lista) - 1)
    
    return lista


def remover_posicao(lista):
    qtd = int(input('\nQuantos elementos remover?\n> '))
        
    for _ in range(qtd):
        pos = int(input('Qual posição a remover?\n> '))
        lista.pop(pos)
    
    return lista


def remover_todos(lista):
    lista = []
    
    return lista


def contar(lista):
    menu_contar = '\n> > > CONTAR < < <\n'
    menu_contar += '1 - Números Pares\n'
    menu_contar += '2 - Números Ímpares\n'
    menu_contar += '3 - Números Positivos\n'
    menu_contar += '4 - Números Negativos\n'
    menu_contar += '5 - Números Nulos\n'
    menu_contar += '6 - Números Primos\n'
    menu_contar += '\nOpção >>> '
    
    opcao_contar = int(input(menu_contar))
    
    if opcao_contar == 1:
        pares = contar_pares(lista)
        print(f'São {pares} números pares')        
    elif opcao_contar == 2:
        impares = contar_impares(lista)
        print(f'São {impares} números ímpares') 
    elif opcao_contar == 3:
        positivos = contar_positivos(lista)
        print(f'São {positivos} números positivos') 
    elif opcao_contar == 4:
        negativos = contar_negativos(lista)
        print(f'São {negativos} números negativos')
    elif opcao_contar == 5:
        nulos = contar_nulos(lista)
        print(f'São {nulos} números nulos')
    elif opcao_contar == 6:
        primos = contar_primos(lista)
        print(f'São {primos} números primos')
        
    else:
        print('\nOpção Inválida!')
        
    if continuar():
        contar(lista)
    else:
        input('Aperte ENTER para continuar... \n')
        menu_principal(lista)


def contar_pares(vetor):
    num_pares = 0
    
    for num in vetor:
        if eh_par(num):
            num_pares += 1
    
    return num_pares


def contar_impares(vetor):
    num_impares = 0
    
    for num in vetor:
        if not eh_par(num):
            num_impares += 1
    
    return num_impares


def contar_positivos(vetor):
    num_positivos = 0
    
    for num in vetor:
        if eh_positivo(num):
            num_positivos += 1
    
    return num_positivos


def contar_negativos(vetor):
    num_negativos = 0
    
    for num in vetor:
        if not eh_positivo(num) and num != 0:
            num_negativos += 1
    
    return num_negativos


def contar_nulos(lista):
    num_nulos = 0
    
    for num in lista:
        if num == 0:
            num_nulos += 1
    
    return num_nulos


def contar_primos(lista):
    num_primos = 0
    
    for num in lista:
        if num_divisores(num) == 2:
            num_primos += 1
    
    return num_primos


def num_divisores(num):
    div = 0
    
    for i in range(1, num + 1):
        if num % i == 0:
            div += 1
    
    return div


def eh_positivo(num):
    if num > 0:
        return True
    else:
        return False


def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


def media(lista):
    print('> > > CALCULAR MÉDIA < < <')
    soma = 0
    
    for num in lista:
        soma += num
    
    if len(lista) == 0:
        print('Lista vazia, impossível calcular')
    else:
        media = soma / len(lista)
        print(f'A média dos elementos da lista é {media:.2f}')
    
    input('Aperte ENTER para continuar... \n')
    menu_principal(lista)


def continuar():
    continuar = 'Deseja continuar?\n' \
            + 'S - Continuar(Inserir)\n' \
            + 'N - Voltar ao menu principal\n> '
        
    verificar_continuar = input(continuar).upper()
    print(verificar_continuar)
    
    if verificar_continuar == 'S':
        return True
    else:
        return False


main()
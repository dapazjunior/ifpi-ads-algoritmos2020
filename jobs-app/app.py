import os
import json

def main():
    
    # inicializar (recuperar banco de dados)
    celulares = inicializar('celulares.bd')

    menu = tela_principal()
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            # criar celular
            celular = novo_celular()

            # salvar celular
            celulares.append(celular)

        elif opcao == 2:
            mostrar_celulares(celulares)
        
        elif opcao == 3:
            pesquisar_celular(celulares)
        
        else:
            print('Opção inválida!\n')
            
        
        input('\n<enter> to continue...')
        opcao = int(input(menu))
    
    # finalizar (salvar banco)
    finalizar('celulares.bd', celulares)


def tela_principal():
    menu = '***** App Jobs Cell *****\n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '3 - Pesquisar celular\n'
    menu += '0 - Sair\n'
    menu += '\nOpção >>> '

    return menu


def sub_menu():
    submenu = 'Selecione a opção desejada:\n'
    submenu += '1 - Mostrar detalhes\n'
    submenu += '2 - Remover registro\n'
    submenu += '3 - Editar celular\n'
    submenu += '4 - Duplicar registro\n'
    submenu += '0 - Concluir pesquisa\n'
    submenu += '\nOpção >>> '

    return submenu


def novo_celular():
    print('Adicionando novo celular')

    # obter dados
    nome = input('Nome: ')
    marca = input('Marca: ')
    tela = input('Tela("): ')
    valor = float(input('Valor (R$): '))
    cam_frontal = input('Camera frontal(sim/não): ')

    celular = {}
    celular['nome'] = nome
    celular['marca'] = marca
    celular['tela'] = tela
    celular['valor'] = valor
    celular['cam_frontal'] = cam_frontal

    return celular


def mostrar_celulares(celulares):
    qtd = len(celulares)
    print(f'Listando {qtd} celulares\n')

    for celular in celulares:
        print_nome_marca(celular)


def print_detalhes(celular):
    print('Nome: ', celular['nome'])
    print('Marca: ', celular['marca'])
    print('Tela: ', celular['tela'])
    valor = celular['valor']
    print(f'Valor: R$ {valor:.2f}')
    print('Possui câmera frontal: ', celular['cam_frontal'])
    print(12 * '---')


def print_nome_marca(celular):
    print('Nome: ', celular['nome'])
    print('Marca: ', celular['marca'])
    print(12 * '---')


def pesquisar_celular(celulares):
    opcao = int(input('Digite a opção referente ao tipo de pesquisa\n1 - Nome\n2 - Marca\n> '))
    busca = []

    if opcao == 1:
        busca = pesquisa_nome(celulares)

    elif opcao == 2:
        busca = pesquisa_marca(celulares)
    
    else:
        print('Opção inválida!')
        pesquisar_celular(celulares)

    if len(busca) > 0:
        menu = sub_menu()
        opcao = int(input(menu))

        if opcao == 1:
            detalhar_celular(busca, celulares)
        
        elif opcao == 2:
            remover_celular(busca, celulares)
        
        elif opcao == 3:
            editar_celular(busca, celulares)
        
        elif opcao == 4:
            duplicar_celular(busca, celulares)
        
        elif opcao == 5:
            main()
        
        else:
            print('Opção inválida!')
            opcao = int(input(menu))


def detalhar_celular(busca, celulares):
    for num in busca:
        print(f'ID celular: {num}')
        print_nome_marca(celulares[num])
    
    id_cel = int(input('Digite o ID do celular a detalhar: '))
    if id_cel in busca:
        print_detalhes(celulares[id_cel])
    else:
        print('ID fora do intervalo da busca!\n')
        detalhar_celular(busca, celulares)


def remover_celular(busca, celulares):
    for num in busca:
        print(f'ID Celular: {num}')
        print('Celular:', celulares[num]['nome'])
        print('---'*12)
    
    id_cel = int(input('Digite o ID do celular a ser removido:\n> '))
    
    if id_cel in busca:
        print('Celular', celulares[id_cel]['nome'], 'removido com sucesso!')
        del(celulares[id_cel])
    else:
        print('ID fora do intervalo da busca!\n')
        remover_celular(busca, celulares)


def editar_celular(busca, celulares):
    for num in busca:
        print(f'ID Celular: {num}')
        print('Celular:', celulares[num]['nome'])
        print('---'*12)
    
    id_cel = int(input('Digite o ID do celular a ser editado:\n> '))
    
    celular = novo_celular()
    celulares[id_cel] = celular


def duplicar_celular(busca, celulares):
    for num in busca:
        print(f'ID Celular: {num}')
        print('Celular:', celulares[num]['nome'])
        print('---'*12)
    
    id_cel = int(input('Digite o ID do celular a ser duplicado:\n> '))
    celulares.append(celulares[id_cel])


def pesquisa_nome(celulares):
    id_cel = 0
    busca = []
    print('Pesquisar por nome\n')
    pesquisa = input('Buscar: ').upper()
    for celular in celulares:
        if pesquisa in celular['nome'].upper():
            print_nome_marca(celular)
            busca.append(id_cel)
        id_cel += 1
    
    return busca


def pesquisa_marca(celulares):
    id_cel = 0
    busca = []
    print('Pesquisar por marca\n')
    pesquisa = input('Buscar: ').upper()
    for celular in celulares:
        if pesquisa in celular['marca'].upper():
            print_nome_marca(celular)
            busca.append(id_cel)
        id_cel += 1
    
    return busca


def inicializar(nome_arquivo):
    celulares_carregados = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        celulares_carregados = json.loads(dados)
    
    return celulares_carregados


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close


# Rodar App
main()

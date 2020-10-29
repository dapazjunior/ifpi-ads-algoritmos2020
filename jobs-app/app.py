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
        
        input('\n<enter> to continue...')
        opcao = int(input(menu))
    
    # finalizar (salvar banco)
    finalizar('celulares.bd', celulares)


def tela_principal():
    menu = '***** App Jobs Cell *****\n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '0 - Sair\n'
    menu += '\nOpção >>> '

    return menu


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
    print(f'Listando {qtd} celulares')

    for celular in celulares:
        print('Nome: ', celular['nome'])
        print('Marca: ', celular['marca'])
        print('Tela: ', celular['tela'])
        print('Valor: ', celular['valor'])
        print('Possui câmera frontal: ', celular['cam_frontal'])
        print(12 * '---')


def inicializar(nome_arquivo):
    celulares_carregados = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        celulares_carregados = json.loads(dados)
    
    return celulares_carregados


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close


# Rodar App
main()

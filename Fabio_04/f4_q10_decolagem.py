def main():
    qtd_containers = int(input('Quantidade de containers: '))

    peso_carga = verificar_containers(qtd_containers)
    
    print('\nVERIFICAÇÃO DE PASSAGEIROS: ')
    total_bagagens, total_passageiros = verificar_passageiros()

    peso_passageiros = total_passageiros * 70
    peso_bagagens = total_bagagens * 10

    peso_total_pass = peso_bagagens + peso_passageiros

    volume_combustivel = verificar_combustivel(peso_total_pass, peso_carga)

    print('\n> > > > > >    INFORMAÇÕES DO VÔO    < < < < < <')
    print(f'Quantidade de passageiros: {total_passageiros}')
    print(f'Quantidade de volumes de bagagem: {total_bagagens}')
    print(f'Peso dos passageiros: {peso_total_pass} kg')
    print(f'Peso da carga: {peso_carga} kg')
    print(f'Combustível possível: {volume_combustivel:.1f} litros')

    if volume_combustivel >= 10000:
        print('\nDECOLAGEM AUTORIZADA!')
    else:
        print('\nCombustível insuficiente!\nDECOLAGEM NÃO AUTORIZADA!')


def verificar_containers(qtd_containers):
    num_container = 1
    soma_peso_containers = 0

    while qtd_containers != 0:
        peso_container = float(input(f'Digite o peso do container {num_container}: '))

        soma_peso_containers += peso_container

        qtd_containers -= 1
        num_container += 1
    
    return soma_peso_containers


def verificar_passageiros():
    num_passageiros = 0
    num_bagagens = 0
    
    while True:
        num_bilhete = int(input('Número do bilhete: '))
        if num_bilhete == 0:
            break
        
        num_passageiros += 1
        
        qtd_bagagens = int(input('Quantidade de bagagens: '))
        num_bagagens += qtd_bagagens

    return num_bagagens, num_passageiros


def verificar_combustivel(peso_total_pass, peso_carga):
    peso_comb = 500000 - peso_carga - peso_total_pass
    litros_comb = peso_comb / 1.5
    return litros_comb


main()

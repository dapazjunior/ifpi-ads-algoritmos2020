import math

def main():
    n = int(input('Digite a quantidade de bois: '))
    maior = 0
    menor = math.inf
    contador = 0

    id_maior = 0
    id_menor = 0

    while contador < n:
        num_id = input('Número de identificação: ')
        peso = float(input(f'Peso do boi: '))

        if peso > maior:
            maior = peso
            id_maior = num_id
        
        if peso < menor:
            menor = peso
            id_menor = num_id
        
        contador += 1
    

    print('\n>>> RELATÓRIO <<<')
    print(f'Maior boi: {id_maior}')
    print(f'Peso do maior boi: {maior} kg')
    print(f'Menor boi: {id_menor}')
    print(f'Peso do menor boi: {menor} kg')

        
main()

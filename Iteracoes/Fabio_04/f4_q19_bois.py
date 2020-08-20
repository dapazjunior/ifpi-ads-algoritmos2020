from math import inf
def main():
    boi_gordo = 0
    boi_magro = inf
    
    while True:
        num_id = int(input('Número de identificação: '))
        
        if num_id == 0:
            break
        
        peso = float(input('Peso da candidata: '))
        print('')
        
        if peso > boi_gordo:
            boi_gordo = peso
            id_boi_gordo = num_id
        
        if peso < boi_magro:
            boi_magro = peso
            id_boi_magro = num_id
        
    
    print(f'Boi mais magro: {id_boi_magro} - Peso: {boi_magro:.1f} kg')
    print(f'Boi mais gordo: {id_boi_gordo} - Peso: {boi_gordo:.1f} kg')


main()

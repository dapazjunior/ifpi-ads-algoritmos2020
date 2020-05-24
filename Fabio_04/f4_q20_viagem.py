def main():
    dist_total = 0
    combustivel_total = 0
    
    while dist_total < 600 and combustivel_total < 50:
        dist_trecho = float(input('Distância percorrida desde a última medição: '))
        combustivel_trecho = float(input('Combustível consumido no trecho: '))
        
        dist_total += dist_trecho
        combustivel_total += combustivel_trecho
        
    combustivel_restante = 50 - combustivel_total
    
    if dist_total >= 600:
        print(f'O carro chegou ao seu destino! Ainda restam {combustivel_restante} litros.')
    else:
        print('O combustível acabou antes do destino!')


main()

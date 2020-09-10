def main():
    distancia = int(input())
    comb_gasto = float(input())
    
    consumo = distancia / comb_gasto
    
    print(f'{consumo:.3f} km/l')


main()